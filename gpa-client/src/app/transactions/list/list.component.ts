import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IAngularMyDpOptions, IMyDateModel } from 'angular-mydatepicker';
import * as moment from 'moment';
import { map } from 'rxjs';
import { Account } from 'src/app/account/account.model';
import { AccountService } from 'src/app/account/services/account.service';
import { TransactionsService } from '../services/transaction-service.service';
import { Transaction, TransactionType } from '../transaction.model';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss'],
})
export class ListComponent implements OnInit {
  transactions: Transaction[] = [];
  userAccounts: Account[] = [];

  debit = TransactionType.DEBIT;
  DATE_FORMAT = 'YYYY-MM-DD';

  myDpOptions: IAngularMyDpOptions = { dateRange: true };
  dateModel: IMyDateModel | null = { isRange: true };
  filterObj = {
    account_number: '',
    date_start: '',
    date_end: '',
  };

  constructor(
    private activatedRoute: ActivatedRoute,
    private transactionsService: TransactionsService,
    private accountsService: AccountService
  ) {}

  ngOnInit(): void {
    this.dateModel = {
      isRange: true,
      singleDate: undefined,
      dateRange: {
        beginJsDate: new Date(),
        endJsDate: new Date(),
      },
    };

    const queryParam$ = this.activatedRoute.queryParamMap.pipe(
      map((param) => param.get('account_number'))
    );

    queryParam$.subscribe((res) => {
      const today = moment();
      this.filterObj = {
        ...this.filterObj,
        date_start: moment().add(-7, 'days').format(this.DATE_FORMAT),
        date_end: today.format(this.DATE_FORMAT),
        account_number: res || '',
      };
      this.loadTransactions();
      this.loadAccounts();
    });
  }

  loadTransactions() {
    this.transactionsService.getTransactionByPeriod(this.filterObj).subscribe({
      next: (res) => {
        this.transactions = res;
      },
      error: (err) => {
        console.error(err);
      },
    });
  }

  loadAccounts() {
    this.accountsService.getAccounts().subscribe({
      next: (res) => {
        this.userAccounts = res;
      },
      error: (err) => {
        console.error(err);
      },
    });
  }

  // optional date changed callback
  onDateChanged(event: IMyDateModel): void {
    if (event.isRange) {
      this.filterObj.date_start = moment
        .unix(Number(event.dateRange?.beginEpoc))
        .format(this.DATE_FORMAT);
      this.filterObj.date_end = moment
        .unix(Number(event.dateRange?.endEpoc))
        .format(this.DATE_FORMAT);
    }
  }

  onAccountNumberChange(event: any) {
    this.filterObj = {
      ...this.filterObj,
      account_number: event.target.value,
    };
  }
}
