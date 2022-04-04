"""Module file"""
# encoding: utf-8

# Force loading of models, so they are taken into account when we run migration commands.
from app.account.repository.account import Account
from app.transactions.repository.transaction import Transaction
from app.user.repository.user import User
