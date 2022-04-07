import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserAccountService } from 'src/app/user/services/user-account.service';

@Component({
  selector: 'app-login-screen',
  templateUrl: './login-screen.component.html',
  styleUrls: ['./login-screen.component.scss'],
})
export class LoginScreenComponent implements OnInit {
  loginForm = this.fb.group({
    username: ['', [Validators.required]],
    password: ['', [Validators.required]],
  });

  constructor(
    private userAccountService: UserAccountService,
    private router: Router,
    private fb: FormBuilder
  ) {}

  ngOnInit(): void {
    if (this.userAccountService.isLoggedIn()) {
    }
  }

  singIn() {
    const username = this.loginForm.get(['username'])?.value;
    const password = this.loginForm.get(['password'])?.value;

    const result = this.userAccountService.login(username, password).subscribe({
      next: (res) => {
        this.router.navigate(['accounts']);
      },
      error: (err) => {
        console.log(err);
      },
    });
    console.log(result);
  }
}
