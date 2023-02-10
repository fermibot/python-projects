(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-20 *)


Module[{paths},
  paths =
      ToExpression /@
          StringSplit[
            Import[StringReplace[NotebookFileName[], ".nb" -> ".txt"]], "\n"];
  paths = GroupBy[paths, Length@# &];
  Framed[Graphics[{Opacity@0.1,
    Line[RandomReal[{-0.15, 0.15}, {Length@#, 2}] + #]} & /@ #,
    PlotRange -> {{0, 10}, {0, 10}}, ImageSize -> 500]] & /@
      Values[paths]
] // Column