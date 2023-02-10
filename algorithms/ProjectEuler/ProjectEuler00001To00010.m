(* Mathematica Package *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)

(* :Title: ProjectEuler_00001_to_00010 *)
(* :Context: ProjectEuler_00001_to_00010` *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-19 *)

(* :Package Version: 0.1 *)
(* :Mathematica Version: *)
(* :Copyright: (c) 2019 Alcatraz *)
(* :Keywords: *)
(* :Discussion: *)

BeginPackage["ProjectEuler00001To00010`"];
(* Exported symbols added here with SymbolName::usage *)

ProjectEuler00001::"";
ProjectEuler00002::"";
ProjectEuler00003::"";
ProjectEuler00004::"";
ProjectEuler00005::"";
ProjectEuler00006::"";
ProjectEuler00007::"";
ProjectEuler00008::"";
ProjectEuler00009::"";

Begin["`Private`"];

ProjectEuler00001 :=
    Total[Select[Range[999], Last[QuotientRemainder[#, 3]] == 0 || Last[QuotientRemainder[#, 5]] == 0 &]];


ProjectEuler00002 :=
    Module[{sum = 0, n = 0},
      While[True,
        If[EvenQ[Fibonacci[n]], sum += Fibonacci[n]]; n += 1;
        If[Fibonacci[n] > 4000000, Break[]]];
      sum
    ];

ProjectEuler00003 := Max@Select[First /@ FactorInteger[600851475143], PrimeQ[#] &];

ProjectEuler00004 := Max[Union @@ (Select[#, PalindromeQ@# &] & /@ Outer[Times, Range[100, 999], Range[100, 999]])];

ProjectEuler00005 := Module[{factors =
    Union @@
        DeleteCases[
          Table[Join @@
              DeleteCases[
                Select[#, #[[1]] == integer &] & /@ (FactorInteger[#] & /@
                    Range[20]), {}], {integer, Range@20}], {}], relevants},
  relevants = Union[#[[1]] & /@ factors];
  Times @@
      Table[
        Power[relevant,
          Max[
            (Select[factors, #[[1]] == relevant &][[;; , 2]])]], {relevant, relevants}]
];

ProjectEuler00006 := Subtract[Power[Total[Range[100]], 2], Total[Power[#, 2] & /@ Range[100]]];

ProjectEuler00007 := Prime[10001];

ProjectEuler00008 := Module[{number =
    7316717653133062491922511967442657474235534919493496983520312774506
  3262395783180169848018694788518438586156078911294949545950173795833195
  2853208805511125406987471585238630507156932909632952274430435576689664
  8950445244523161731856403098711121722383113622298934233803081353362766
  1428280644448664523874930358907296290491560440772390713810515859307960
  8667017242712188399879790879227492190169972088809377665727333001053367
  8812202354218097512545405947522435258490771167055601360483958644670632
  4415722155397536978179778461740649551492908625693219784686224828397224
  1375657056057490261407972968652414535100474821663704844031998900088952
  4345065854122758866688116427171479924442928230863465674813919123162824
  5861786645835912456652947654568284891288314260769004224219022671055626
  3211111093705442175069416589604080719840385096245544436298123098787992
  7244284909188845801561660979191338754992005240636899125607176060588611
  6467109405077541002256983155200055935729725716362695618826704282524836
  00823257530420752963450}, number = IntegerDigits[number];
Max[Times @@@ (number[[# ;; # + 12]] & /@ Range[988])]
];

ProjectEuler00009 := With[{n = 1000},
  Select[Select[Join @@ Join @@ Table[{a, b, c}, {a, Range@n}, {b, Range@n}, {c, Range@n}], Total[#] == n&],
    Power[Max[#, 2] == Total[(Power[#, 2]& /@ Reverse[Sort[#]][[2 ;;]])&]]
  ]
];

ProjectEuler00010 := Total[Prime[#]& /@ Range[148933]];


End[]; (* `Private` *)

EndPackage[]