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

  public getTransactionByPeriod(account_number: number, period: string) {
    let params = new HttpParams()
      .append('account_number', account_number)
      .append('period', period);

    return this.http.get<Transaction>('/api/v1/transaction', { params });
  }
}
