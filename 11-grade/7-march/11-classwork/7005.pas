var
  tmp: integer;

function corner(x, y, z: integer): boolean;
begin
  corner := (x + y + z = 180); 
end;

function f(x, A: integer): boolean;
begin
  f := ((corner(37, A, x + 45) = corner(A, x, 90)) and ((A + 23 >= 120)))
end;

begin

  
  for var A := 1 to 256 do
  begin
    tmp := 0;
    for var x := 1 to 256 do
    begin
      if (f(x, A) = True) then
        tmp := tmp + 1
    end;
    if (tmp = 256) then
      writeLn(A)
  end;

end.