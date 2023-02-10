(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-15 *)


Module[{number = 1, maximum = 1000000, dBPalindromes = {}},
  While[number < maximum,
    If[And @@ (PalindromeQ /@ (Characters[
      IntegerString[number, #]] & /@ {2, 10})),
      AppendTo[dBPalindromes, number]];
    number += 1;
  ];
  dBPalindromes
] // Total

