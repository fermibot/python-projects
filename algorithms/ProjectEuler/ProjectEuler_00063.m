(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-16 *)

Length@Select[
  Join @@ Table[{b, Power[a, b]}, {a, 1, 9}, {b, 1, 100}], #[[1]] ==
      IntegerLength@#[[2]] &]


(*Answer 49*)