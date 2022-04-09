import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Transaction } from '../transaction.model';

@Injectable({
  providedIn: 'root',
})
export class TransactionsService {
  constructor(private http: HttpClient) {}

  public registerTransaction(transaction: Transaction) {
    return this.http.post<Transaction>('/api/v1/transaction', transaction);
  }

  public getTransactionByPeriod(filterObj: any) {
    let params = new HttpParams();

    for (let filter of ['account_number', 'date_start', 'date_end']) {
      if (!!filterObj[filter]) {
        params = params.append(filter, filterObj[filter]);
      }
    }

    return this.http.get<Transaction[]>('/api/v1/transaction', { params });
  }
}
