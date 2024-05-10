from django.urls import path
from .views import BudgetListCreateView, BudgetDetailView, ExpenseListCreateView, ExpenseDetailView, SavingsGoalListCreateView, SavingsGoalDetailView

urlpatterns = [
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('savings-goals/', SavingsGoalListCreateView.as_view(), name='savings-goal-list-create'),
    path('savings-goals/<int:pk>/', SavingsGoalDetailView.as_view(), name='savings-goal-detail'),
]
