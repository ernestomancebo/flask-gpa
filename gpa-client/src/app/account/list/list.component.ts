import { Component, OnInit } from '@angular/core';
import { Account } from '../account.model';
import { AccountService } from '../services/account.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss'],
})
export class ListComponent implements OnInit {
  accounts: Account[] = [];

  constructor(private accountService: AccountService) {}

  ngOnInit(): void {
    this.fetchAccounts();
  }

  fetchAccounts() {
    this.accountService.getAccounts().subscribe({
      next: (res) => {
        this.accounts = res;
      },
      error: (err) => {
        console.error(err);
      },
    });
  }
}
