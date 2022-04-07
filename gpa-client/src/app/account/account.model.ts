export class Account {
  constructor(
    public account_number: number,
    public owner: number,
    public description: string,
    public balance: number,
    public creation_date: Date
  ) {}
}
