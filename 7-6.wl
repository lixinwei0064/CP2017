(* ::Package:: *)

Clear["Global`*"]
BeginPackage["hermite`"]
hermite::usage="hermite polynomials"
hermite[0,x_]:=1
hermite[1,x_]:=2x
hermite[n_,x_]:=2x hermite[n-1,x]-2(n-1) hermite[n-2,x]//Expand
EndPackage[]



