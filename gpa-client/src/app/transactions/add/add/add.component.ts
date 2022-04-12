import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AccountService } from 'src/app/account/services/account.service';
import { Account } from '../../../account/account.model';
import { TransactionsService } from '../../services/transaction-service.service';
import { Transaction, TransactionType } from '../../transaction.model';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.scss'],
})
export class AddComponent implements OnInit {
  transactionTypes = [TransactionType.CREDIT, TransactionType.DEBIT];
  userAccounts: Account[] = [];

  transactionForm = this.fb.group({
    account: ['', Validators.required],
    amount: ['', Validators.required],
    note: ['', Validators.maxLength(100)],
    type: ['', Validators.required],
  });

  constructor(
    private fb: FormBuilder,
    private accountsService: AccountService,
    private transactionsService: TransactionsService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadAccounts();
  }

  addTransaction() {
    const transaction: Transaction = {
      id: 0,
      account_id: this.transactionForm.get('account')?.value,
      amount: this.transactionForm.get('amount')?.value,
      note: this.transactionForm.get('note')?.value,
      transaction_type: this.transactionForm.get('type')?.value,
    };

    this.transactionsService.registerTransaction(transaction).subscribe({
      next: (res) => {
        if (confirm('Would you like to add a new transaction')) {
          this.transactionForm.reset();
          return;
        }
        this.router.navigate(['/transactions']);
      },
      error: (err) => {},
    });
  }

  loadAccounts() {
    this.accountsService.getAccounts().subscribe({
      next: (res) => {
        this.userAccounts = res;
      },
      error: (err) => {
        alert(`There was an error:\n${err.error.message}`);
        console.error(err);
      },
    });
  }
}
