(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-15 *)


ClearAll[TruncatablePrimeQ];

TruncatablePrimeQ[number_] := Module[{iG = IntegerDigits@number},
  And @@ (PrimeQ /@ ((FromDigits[iG[[1 ;; #]]] & /@ Range[Length@iG]) ~
      Join ~ (FromDigits[iG[[-# ;; -1]]] & /@ Range[Length@iG])))
]

Module[{truncatablePrimes = List[], primeNumber = 11, prime},
  While[Length@truncatablePrimes <= 10,
    prime = Prime[primeNumber];
    If[TruncatablePrimeQ@prime, AppendTo[truncatablePrimes, prime]];
    primeNumber += 1;
  ];
  truncatablePrimes // Total
]

