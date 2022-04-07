import { Component, OnInit } from '@angular/core';
import * as moment from 'moment';
import { Transaction, TransactionType } from '../transaction.model';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss'],
})
export class ListComponent implements OnInit {
  transactions: Transaction[] = [];
  debit = TransactionType.DEBIT;

  constructor() {}

  ngOnInit(): void {
    this.transactions = [
      {
        id: 55,
        account_id: 'adad',
        note: 'adsadsada',
        occurred_at: new Date(moment.now()),
        performed_by: 22,
        transaction_type: TransactionType.CREDIT,
        amount: 40,
        period: '2021',
      },
      {
        id: 55,
        account_id: 'adad',
        note: '',
        occurred_at: new Date(moment.now()),
        performed_by: 22,
        transaction_type: TransactionType.DEBIT,
        amount: 40,
        period: '2021',
      },
      {
        id: 55,
        account_id: 'adad',
        note: 'adsadsada',
        occurred_at: new Date(moment.now()),
        performed_by: 22,
        transaction_type: TransactionType.CREDIT,
        amount: 40,
        period: '2021',
      },
    ];
  }
}
