import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { AddComponent } from './add/add/add.component';
import { ListComponent } from './list/list.component';
import { TransactionsRoutingModule } from './transactions-routing.module';

@NgModule({
  declarations: [ListComponent, AddComponent],
  imports: [CommonModule, TransactionsRoutingModule, ReactiveFormsModule],
  exports: [TransactionsRoutingModule],
})
export class TransactionsModule {}
