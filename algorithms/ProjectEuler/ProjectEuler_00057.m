(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-16 *)

Select[Rest[1 + NestList[Divide[1, 2 + #] &, 0, 1000]],
  IntegerLength@Numerator@# > IntegerLength@Denominator@# &] // Length