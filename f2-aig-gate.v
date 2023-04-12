// Benchmark "f2.eqn" written by ABC on Fri Feb 24 14:23:00 2023

module \f2.eqn  ( 
    b, d, g, f, e,
    f2, f2_min, f2_fact  );
  input  b, d, g, f, e;
  output f2, f2_min, f2_fact;
  wire new_n9_, new_n10_, new_n11_, new_n12_, new_n13_, new_n15_, new_n16_;
  inv1   g0(.a(g), .O(new_n9_));
  oai21  g1(.a(e), .b(d), .c(b), .O(new_n10_));
  inv1   g2(.a(b), .O(new_n11_));
  inv1   g3(.a(d), .O(new_n12_));
  oai21  g4(.a(f), .b(new_n12_), .c(new_n11_), .O(new_n13_));
  aoi21  g5(.a(new_n13_), .b(new_n10_), .c(new_n9_), .O(f2));
  oai21  g6(.a(f), .b(b), .c(d), .O(new_n15_));
  oai21  g7(.a(e), .b(new_n11_), .c(new_n12_), .O(new_n16_));
  aoi21  g8(.a(new_n16_), .b(new_n15_), .c(new_n9_), .O(f2_min));
  aoi21  g9(.a(new_n16_), .b(new_n15_), .c(new_n9_), .O(f2_fact));
endmodule


