from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import FoundItem, LostItem, ClaimRequest
from .forms import ClaimForm

def claim_lost_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)

    if request.method == "POST":
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.lost_item = item
            claim.save()

            # 🔥 Автоматически помечаем предмет как найденный
            item.is_found = True
            item.save()

            messages.success(request, "Заявка отправлена! Предмет отмечен как найденный.")
            return redirect("lost_items_list")

    else:
        form = ClaimForm()

    return render(request, "items/claim_lost_item.html", {"form": form, "item": item})


def claim_found_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id)

    if request.method == "POST":
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.found_item = item
            claim.save()

            # 🔥 Автоматически помечаем предмет как "Забранный"
            item.is_claimed = True
            item.save()

            messages.success(request, "Заявка отправлена! Предмет отмечен как забранный.")
            return redirect("found_items_list")

    else:
        form = ClaimForm()

    return render(request, "items/claim_found_item.html", {"form": form, "item": item})

from .models import LostItem, FoundItem
from .forms import LostItemForm, FoundItemForm


def index(request):
    return render(request,  "base.html" )

def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def delete_lost_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    item.delete()
    return redirect("admin_items_list")

@user_passes_test(is_staff_user)
def delete_found_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id)
    item.delete()
    return redirect("admin_items_list")

def lost_items_list(request):
    items = LostItem.objects.all()
    return render(request, "items/lost_items_list.html", {"items": items})

def found_items_list(request):
    items = FoundItem.objects.all()
    return render(request, "items/found_items_list.html", {"items": items})

def add_lost_item(request):
    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lost_items_list")
    else:
        form = LostItemForm()
    return render(request, "items/item_form.html", {"form": form})

def add_found_item(request):
    if request.method == "POST":
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("found_items_list")
    else:
        form = FoundItemForm()
    return render(request, "items/item_form.html", {"form": form})


@user_passes_test(is_staff_user)
def admin_items_list(request):
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()
    return render(request, "items/admin_items_list.html", {"lost_items": lost_items, "found_items": found_items})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ClaimRequest

@login_required
def my_claims(request):
    """Страница для просмотра заявок пользователя"""
    claims = ClaimRequest.objects.filter(name=request.user.username)  # Фильтруем по имени
    return render(request, "items/my_claims.html", {"claims": claims})
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@staff_member_required
def approve_claim(request, claim_id):
    """Администратор подтверждает заявку"""
    claim = get_object_or_404(ClaimRequest, id=claim_id)
    claim.approved = True
    claim.save()
    messages.success(request, "Заявка подтверждена!")
    return redirect("my_claims")

from django.db.models import Q  # 🔥 Импортируем для фильтрации

def lost_items_list(request):
    search_query = request.GET.get("search", "")  # Получаем поисковый запрос
    items = LostItem.objects.all()

    if search_query:
        items = items.filter(Q(name__icontains=search_query) | Q(location__icontains=search_query))

    return render(request, "items/lost_items_list.html", {"items": items, "search_query": search_query})

def found_items_list(request):
    search_query = request.GET.get("search", "")  # Получаем поисковый запрос
    items = FoundItem.objects.all()

    if search_query:
        items = items.filter(Q(name__icontains=search_query) | Q(location__icontains=search_query))

    return render(request, "items/found_items_list.html", {"items": items, "search_query": search_query})
