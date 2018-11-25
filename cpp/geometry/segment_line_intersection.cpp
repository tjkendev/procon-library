typedef int PType;
struct Point {
  PType x, y;
};
 
PType dot3(Point o, Point a, Point b) {
  return (a.x - o.x) * (b.x - o.x) + (a.y - o.y) * (b.y - o.y);
}
PType cross3(Point o, Point a, Point b) {
  return (a.x - o.x) * (b.y - o.y) - (b.x - o.x) * (a.y - o.y);
}
PType dist2(Point a, Point b) {
  return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
}
 
bool intersect(Point p0, Point p1, Point q0, Point q1) {
  PType c0 = cross3(p0, p1, q0), c1 = cross3(p0, p1, q1);
  PType d0 = cross3(q0, q1, p0), d1 = cross3(q0, q1, p1);
  if(c0 == 0 && c1 == 0) {
    PType e0 = dot3(p0, p1, q0);
    PType e1 = dot3(p0, p1, q1);
    if( !(e0 < e1) ) {
      swap(e0, e1);
    }
    return e0 <= dist2(p0, p1) && 0 <= e1;
  }
  return (c0 ^ c1) <= 0 && (d0 ^ d1) <= 0;
}