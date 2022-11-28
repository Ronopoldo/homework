var
  num, amount: integer;

begin
  amount := 0;
  num := -1;
  while (num <> 0) do
  begin
    readLn(num);
    if ((num <> 0) and (num mod 2 = 0) and (num mod 5 = 0))
      then amount := amount + 1;
  end;
  writeLn(amount);
end.