import { Component, OnInit } from '@angular/core';
import { UserAccountService } from './user/services/user-account.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  title = 'gpa-client';

  constructor(private userService: UserAccountService) {}

  ngOnInit(): void {}
}
