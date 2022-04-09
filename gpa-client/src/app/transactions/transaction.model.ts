import { Account } from '../account/account.model';

export enum TransactionType {
  DEBIT = 'Debit',
  CREDIT = 'Credit',
}

export class Transaction {
  constructor(
    public id: number | null,
    public transaction_type: TransactionType,
    public amount: number,
    public account_id: string,
    public account?: Account,
    public performed_by?: number | null,
    public note?: string,
    public occurred_at?: Date,
    public period?: string
  ) {}
}
