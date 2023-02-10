(* Mathematica Package *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)

(* :Title: test *)
(* :Context: test` *)
(* :Author: Alcatraz *)
(* :Date: 2019-08-16 *)

(* :Package Version: 0.1 *)
(* :Mathematica Version: *)
(* :Copyright: (c) 2019 Alcatraz *)
(* :Keywords: *)
(* :Discussion: *)

BeginPackage["test`"]
(* Exported symbols added here with SymbolName::usage *)

Begin["`Private`"]


ClearAll[NextLargestInteger]
Options[NextLargestInteger] = {"Echo" -> False};
NextLargestInteger[integer_Integer, OptionsPattern[]] :=
    Module[{integerLength = IntegerLength@integer},
      If[integerLength == 1,
        integer,
        Module[{permutationTrack = 2, nextLargestInteger = integer,
          integerDigits = IntegerDigits@integer, largerPermutations,
          permutables},
          While[permutationTrack <= integerLength,
            permutables = Take[integerDigits, -permutationTrack];
            largerPermutations =
                Sort[Select[
                  FromDigits /@
                      Permutations[permutables], # > FromDigits[permutables] &]];
            If[! largerPermutations === {},
              nextLargestInteger =
                  FromDigits[
                    Join @@ {Drop[integerDigits, -permutationTrack],
                      IntegerDigits[largerPermutations // First]}];
              If[OptionValue["Echo"], Echo[nextLargestInteger]];
              Break[];,
              None
            ];
            permutationTrack += 1;
          ];
          nextLargestInteger
        ]
      ]
    ]

With[{nextLargestInteger = 1234},
  NestWhileList[# ~
      Join ~ {# // Last} &, {nextLargestInteger}, (# //
      Last != nextLargestInteger) &]
]

Module[{nextLargestInteger = 1234},
  Table[nextLargestInteger = NextLargestInteger[nextLargestInteger],
    200]
]

End[] (* `Private` *)

EndPackage[]