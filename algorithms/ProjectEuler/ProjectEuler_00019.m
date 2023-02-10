(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-14 *)


Length[Select[
  DateRange[DateObject[{1901, 01, 01}], DateObject[{2000, 12, 31}]],
  DayName[#] == Sunday && #[[1, 3]] == 1 &]]