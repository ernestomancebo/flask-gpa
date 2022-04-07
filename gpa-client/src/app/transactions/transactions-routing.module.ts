import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { UserRouteAccessService } from '../user/services/user-route-access.service';
import { AddComponent } from './add/add/add.component';
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
        component: AddComponent,
      },
    ]),
  ],
  exports: [RouterModule],
})
export class TransactionsRoutingModule {}
