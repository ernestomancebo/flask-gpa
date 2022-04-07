import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { AccountService } from '../services/account.service';

@Component({
  selector: 'app-add-account',
  templateUrl: './add-account.component.html',
  styleUrls: ['./add-account.component.scss'],
})
export class AddAccountComponent implements OnInit {
  accountForm = this.fb.group({
    accountnumber: ['', [Validators.required]],
    description: ['', [Validators.required, Validators.maxLength(100)]],
  });

  constructor(
    private fb: FormBuilder,
    private accountService: AccountService
  ) {}

  ngOnInit(): void {}

  addAccount() {
    const [account_number, description] = [
      String(this.accountForm.get('accountnumber')?.value || ''),
      this.accountForm.get('description')?.value,
    ];

    this.accountService.addAccount({ account_number, description }).subscribe({
      next: (response) => console.log('ok'),
      error: (err) => console.log('not ok:', err),
    });
  }
}
