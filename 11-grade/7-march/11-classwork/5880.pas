var
  tmp: integer;


function Max(x1, x2 : integer) : integer;
begin
  if x1 > x2 then
    Max := x1
  else
    Max := x2;
end; 

function triangle(x, y, z: integer): boolean;
begin
  triangle := Max(x, y, z) < (x + y + z - Max(x, y, z)); 
end;

function f(x, A: integer): boolean;
begin
  f := ((triangle(A, 5, x)) <= (Max(x, 11) <= 19) = (not (triangle(23, 13, x))));
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