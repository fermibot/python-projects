(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Alcatraz *)
(* :Date: 2019-07-17 *)


Module[{currentInteger = 1, currentIntegerDigits, currentLength = 0,
  list = {}},
  While[currentLength <= 1000000,
    currentIntegerDigits = IntegerDigits[currentInteger];
    list = list ~ Join ~ currentIntegerDigits;
    currentInteger += 1;
    currentLength += Length@currentIntegerDigits;
  ];
  Times @@
      list[[Power[10, #] & /@ Range[0, Floor[Log10[currentLength]]]]]
]