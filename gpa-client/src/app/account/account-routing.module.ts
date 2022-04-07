import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { UserRouteAccessService } from '../user/services/user-route-access.service';
import { AddAccountComponent } from './add/add-account.component';
import { ListComponent } from './list/list.component';

@NgModule({
  imports: [
    RouterModule.forChild([
      {
        path: '',
        canActivate: [UserRouteAccessService],
        component: ListComponent,
      },
      {
        path: 'add',
        canActivate: [UserRouteAccessService],
        component: AddAccountComponent,
      },
    ]),
  ],
  exports: [RouterModule],
})
export class AccountRoutingModule {}
