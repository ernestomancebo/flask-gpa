export class User {
  constructor(
    public activated: boolean,
    public role: string[],
    public email: string,
    public name: string | null,
    public username: string
  ) {}
}
