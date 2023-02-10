(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-16 *)


Sort /@ Select[
  GatherBy[Power[#, 3] & /@ Range[1, 10000], Sort@IntegerDigits@# &],
  Length@# == 5 &]