import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AngularMyDatePickerModule } from 'angular-mydatepicker';
import { AddComponent } from './add/add/add.component';
import { ListComponent } from './list/list.component';
import { TransactionsRoutingModule } from './transactions-routing.module';

@NgModule({
  declarations: [ListComponent, AddComponent],
  imports: [
    CommonModule,
    TransactionsRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    AngularMyDatePickerModule,
  ],
  exports: [TransactionsRoutingModule],
})
export class TransactionsModule {}
