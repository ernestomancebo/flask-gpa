import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router } from '@angular/router';
import { Observable, of } from 'rxjs';
import { UserAccountService } from './user-account.service';

@Injectable({
  providedIn: 'root',
})
export class UserRouteAccessService implements CanActivate {
  constructor(
    private route: Router,
    // private state: RouterStateSnapshot,
    private userAccountService: UserAccountService
  ) {}

  canActivate(
    route: ActivatedRouteSnapshot
    // state: RouterStateSnapshot
  ): Promise<boolean> | boolean {
    return new Promise((resolve) => {
      try {
        const isLoggedIn = this.userAccountService.isLoggedIn();

        if (isLoggedIn === false) {
          this.route.navigate(['login']);
        }

        resolve(isLoggedIn);
      } catch (e) {
        this.route.navigate(['login']);
        resolve(false);
      }
    });
  }
}
