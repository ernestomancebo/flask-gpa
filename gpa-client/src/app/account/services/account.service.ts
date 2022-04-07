import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Account } from '../account.model';

@Injectable({
  providedIn: 'root',
})
export class AccountService {
  constructor(protected http: HttpClient) {}

  getAccounts() {
    return this.http.get<Account[]>('/api/v1/account');
  }

  getAccountPeriod(account_number: number) {
    let params = new HttpParams().append('account_number', account_number);

    return this.http.get<Account>('/api/v1/account/periods', { params });
  }

  addAccount(account: any) {
    return this.http.post<Account>('/api/v1/account', {
      ...account,
    });
  }
}
