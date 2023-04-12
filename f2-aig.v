// Benchmark "f2.eqn" written by ABC on Wed Feb  8 16:43:21 2023

module f2.eqn  ( 
    b, d, g, f, e,
    f2, f2_min, f2_fact  );
  input  b, d, g, f, e;
  output f2, f2_min, f2_fact;
  wire new_n9_, new_n10_, new_n11_, new_n12_, new_n13_, new_n14_, new_n15_,
    new_n17_, new_n18_, new_n19_, new_n20_, new_n21_;
  assign new_n9_ = ~d & e;
  assign new_n10_ = ~d & ~new_n9_;
  assign new_n11_ = b & ~new_n10_;
  assign new_n12_ = d & f;
  assign new_n13_ = d & ~new_n12_;
  assign new_n14_ = ~b & ~new_n13_;
  assign new_n15_ = ~new_n11_ & ~new_n14_;
  assign f2 = g & ~new_n15_;
  assign new_n17_ = ~b & ~f;
  assign new_n18_ = d & ~new_n17_;
  assign new_n19_ = b & ~e;
  assign new_n20_ = ~d & ~new_n19_;
  assign new_n21_ = ~new_n18_ & ~new_n20_;
  assign f2_min = g & ~new_n21_;
  assign f2_fact = f2_min;
endmodule


