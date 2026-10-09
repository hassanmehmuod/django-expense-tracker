from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(owner=request.user)
    return render(request, "tracker/expense_list.html",  {"expenses": expenses})

@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.owner = request.user
            expense.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()
    return render(request, "tracker/expense_form.html", {"form" : form} )

@login_required    
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, owner=request.user)
    expense.delete()
    return redirect("expense_list")

@login_required
def  edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, owner= request.user)
    if request.method == "POST":
            form = ExpenseForm(request.POST, instance=expense)
            if form.is_valid():
                form.save()
                return redirect("expense_list")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "tracker/expense_form.html", {"form" : form} )
    
