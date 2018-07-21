var fs = require('fs');

// class Stdin
function Stdin() {
  this.__input = null;
  this.__lines = [];
  this.__index = 0;
}
Stdin.prototype.init = function() {
  this.__input = fs.readFileSync('/dev/stdin', 'utf-8');
  this.__lines = this.__input.split("\n");
  this.__index = 0;
}
Stdin.prototype.readline = function() {
  if(this.__index === this.__lines.length) this.init();
  return this.__lines[this.__index++];
};
Stdin.prototype.readlines = function() {
  if(this.__index === this.__lines.length) this.init();
  cur = this.__index; this.__index = this.__lines.length;
  return this.__lines.slice(cur);
};
var stdin = new Stdin;

Array.prototype.imap = function() { return this.map((x)=>parseInt(x)); }
Array.prototype.fmap = function() { return this.map((x)=>parseFloat(x)); }
Array.prototype.smap = function() { return this.map((x)=>String(x)); }
Array.prototype.ffill = function(cb) {
  for(var i=0; i<this.length; ++i) { this[i] = cb(i); } return this;
}
Array.prototype.max = function(cb) {
  if(this.length === 0) return undefined;
  res = cb ? cb(this[0], 0) : this[0];
  for(var i=1; i<this.length; ++i){ var val = cb ? cb(this[i], i) : this[i]; if(res < val) res = val; }
  return res;
}
Array.prototype.min = function(cb) {
  if(this.length === 0) return undefined;
  res = cb ? cb(this[0], 0) : this[0];
  for(var i=1; i<this.length; ++i){ var val = cb ? cb(this[i], i) : this[i]; if(val < res) res = val; }
  return res;
}
Array.prototype.sum = function(cb) {
  if(this.length === 0) return undefined;
  res = cb ? cb(this[0], 0) : this[0];
  for(var i=1; i<this.length; ++i) res += cb ? cb(this[i], i) : this[i];
  return res;
}

Number.prototype.times = function(cb) { res = []; for(var i=0; i<this; ++i) res.push(cb ? cb(i) : i); return res; }

Object.prototype.forEach = function(cb) { Object.keys(this).forEach(cb); }
Object.prototype.map = function(cb) { return Object.keys(this).map(cb); }
