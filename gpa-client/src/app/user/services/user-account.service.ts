import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import * as moment from 'moment';
import { shareReplay, tap } from 'rxjs';
import { User } from '../user.model';

@Injectable({
  providedIn: 'root',
})
export class UserAccountService {
  private _currentUser: User | null = null;

  private set currentUser(value: User | null) {
    this._currentUser = value;
    localStorage.setItem('user', JSON.stringify(value));
  }

  get currentUser() {
    this._currentUser =
      this._currentUser || JSON.parse(localStorage.getItem('user') || '{}');
    return this._currentUser;
  }

  constructor(protected http: HttpClient, protected router: Router) {}

  getAccounts() {
    // TODO: retrieve all the accounts
  }

  addAccount() {
    // TODO: create account
  }

  login(username: string, password: string) {
    // Http basic authentication
    let httpHeaders = new HttpHeaders().append(
      'Authorization',
      'basic ' + btoa(`${username}:${password}`)
    );

    return this.http
      .post<User>(
        '/api/v1/user/authentication',
        {},
        { headers: httpHeaders, withCredentials: true }
      )
      .pipe(
        tap((res) => this.setSession(res)),
        tap((res) => this.setCurrentUser(res)),
        shareReplay()
      );
  }

  private setSession(authResult: any) {
    const { token, time_delta, time_meassure } = authResult['session'];
    const expiresAt = moment().add(time_delta, time_meassure);

    localStorage.setItem('id_token', token);
    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()));
  }

  private setCurrentUser(authResult: any) {
    this.currentUser = authResult['user'];
  }

  logout() {
    this._currentUser = null;
    localStorage.removeItem('id_token');
    localStorage.removeItem('expires_at');
  }

  isLoggedIn() {
    const answer =
      !!this.currentUser && moment().isBefore(this.getExpiration());
    if (!answer) {
      this.logout();
      this.router.navigate(['accounts']);
    }

    return answer;
  }

  isLoggedOut() {
    return !this.isLoggedIn();
  }

  getExpiration() {
    const expiration: string = localStorage.getItem('expires_at') || '';
    const expiresAt = JSON.parse(expiration);
    return moment(expiresAt);
  }
}
