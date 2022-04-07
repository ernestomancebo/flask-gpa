import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { AccountRoutingModule } from './account-routing.module';
import { AddAccountComponent } from './add/add-account.component';
import { ListComponent } from './list/list.component';

@NgModule({
  declarations: [ListComponent, AddAccountComponent],
  imports: [CommonModule, AccountRoutingModule, ReactiveFormsModule],
  exports: [AccountRoutingModule],
})
export class AccountModule {}
