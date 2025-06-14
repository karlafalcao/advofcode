<main>
<article class="day-desc"><h2>--- Day 24: Crossed Wires ---</h2><p>You and The Historians arrive at the edge of a <a href="/2022/day/23">large grove</a> somewhere in the jungle. After the last incident, the Elves installed a small device that monitors the fruit. While The Historians search the grove, one of them asks if you can take a look at the monitoring device; apparently, it's been malfunctioning recently.</p>
<p>The device seems to be trying to produce a number through some boolean logic gates. Each gate has two inputs and one output. The gates all operate on values that are either <em>true</em> (<code>1</code>) or <em>false</em> (<code>0</code>).</p>
<ul>
<li><code>AND</code> gates output <code>1</code> if <em>both</em> inputs are <code>1</code>; if either input is <code>0</code>, these gates output <code>0</code>.</li>
<li><code>OR</code> gates output <code>1</code> if <em>one or both</em> inputs is <code>1</code>; if both inputs are <code>0</code>, these gates output <code>0</code>.</li>
<li><code>XOR</code> gates output <code>1</code> if the inputs are <em>different</em>; if the inputs are the same, these gates output <code>0</code>.</li>
</ul>
<p>Gates wait until both inputs are received before producing output; wires can carry <code>0</code>, <code>1</code> or no value at all. There are no loops; once a gate has determined its output, the output will not change until the whole system is reset. Each wire is connected to at most one gate output, but can be connected to many gate inputs.</p>
<p>Rather than risk getting shocked while tinkering with the live system, you write down all of the gate connections and initial wire values (your puzzle input) so you can consider them in relative safety. For example:</p>
<pre><code>x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -&gt; z00
x01 XOR y01 -&gt; z01
x02 OR y02 -&gt; z02
</code></pre>
<p>Because gates wait for input, some wires need to start with a value (as inputs to the entire system). The first section specifies these values. For example, <code>x00: 1</code> means that the wire named <code>x00</code> starts with the value <code>1</code> (as if a gate is already outputting that value onto that wire).</p>
<p>The second section lists all of the gates and the wires connected to them. For example, <code>x00 AND y00 -&gt; z00</code> describes an instance of an <code>AND</code> gate which has wires <code>x00</code> and <code>y00</code> connected to its inputs and which will write its output to wire <code>z00</code>.</p>
<p>In this example, simulating these gates eventually causes <code>0</code> to appear on wire <code>z00</code>, <code>0</code> to appear on wire <code>z01</code>, and <code>1</code> to appear on wire <code>z02</code>.</p>
<p>Ultimately, the system is trying to produce a <em>number</em> by combining the bits on all wires starting with <code>z</code>. <code>z00</code> is the least significant bit, then <code>z01</code>, then <code>z02</code>, and so on.</p>
<p>In this example, the three output bits form the binary number <code>100</code> which is equal to the decimal number <code><em>4</em></code>.</p>
<p>Here's a larger example:</p>
<pre><code>x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -&gt; mjb
y02 OR x01 -&gt; tnw
kwq OR kpj -&gt; z05
x00 OR x03 -&gt; fst
tgd XOR rvg -&gt; z01
vdt OR tnw -&gt; bfw
bfw AND frj -&gt; z10
ffh OR nrd -&gt; bqk
y00 AND y03 -&gt; djm
y03 OR y00 -&gt; psh
bqk OR frj -&gt; z08
tnw OR fst -&gt; frj
gnj AND tgd -&gt; z11
bfw XOR mjb -&gt; z00
x03 OR x00 -&gt; vdt
gnj AND wpb -&gt; z02
x04 AND y00 -&gt; kjc
djm OR pbm -&gt; qhw
nrd AND vdt -&gt; hwm
kjc AND fst -&gt; rvg
y04 OR y02 -&gt; fgs
y01 AND x02 -&gt; pbm
ntg OR kjc -&gt; kwq
psh XOR fgs -&gt; tgd
qhw XOR tgd -&gt; z09
pbm OR djm -&gt; kpj
x03 XOR y03 -&gt; ffh
x00 XOR y04 -&gt; ntg
bfw OR bqk -&gt; z06
nrd XOR fgs -&gt; wpb
frj XOR qhw -&gt; z04
bqk OR frj -&gt; z07
y03 OR x01 -&gt; nrd
hwm AND bqk -&gt; z03
tgd XOR rvg -&gt; z12
tnw OR pbm -&gt; gnj
</code></pre>
<p>After waiting for values on all wires starting with <code>z</code>, the wires in this system have the following values:</p>
<pre><code>bfw: 1
bqk: 1
djm: 1
ffh: 0
fgs: 1
frj: 1
fst: 1
gnj: 1
hwm: 1
kjc: 0
kpj: 1
kwq: 0
mjb: 1
nrd: 1
ntg: 0
pbm: 1
psh: 1
qhw: 1
rvg: 0
tgd: 0
tnw: 1
vdt: 1
wpb: 0
z00: 0
z01: 0
z02: 0
z03: 1
z04: 0
z05: 1
z06: 1
z07: 1
z08: 1
z09: 1
z10: 1
z11: 0
z12: 0
</code></pre>
<p>Combining the bits from all wires starting with <code>z</code> produces the binary number <code>0011111101000</code>. Converting this number to decimal produces <code><em>2024</em></code>.</p>
<p>Simulate the system of gates and wires. <em>What decimal number does it output on the wires starting with <code>z</code>?</em></p>
</article>
<p>Your puzzle answer was <code>47666458872582</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>After inspecting the monitoring device more closely, you determine that the system you're simulating is trying to <em>add two binary numbers</em>.</p>
<p>Specifically, it is treating the bits on wires starting with <code>x</code> as one binary number, treating the bits on wires starting with <code>y</code> as a second binary number, and then attempting to add those two numbers together. The output of this operation is produced as a binary number on the wires starting with <code>z</code>. (In all three cases, wire <code>00</code> is the least significant bit, then <code>01</code>, then <code>02</code>, and so on.)</p>
<p>The initial values for the wires in your puzzle input represent <em>just one instance</em> of a pair of numbers that sum to the wrong value. Ultimately, <em>any</em> two binary numbers provided as input should be handled correctly. That is, for any combination of bits on wires starting with <code>x</code> and wires starting with <code>y</code>, the sum of the two numbers those bits represent should be produced as a binary number on the wires starting with <code>z</code>.</p>
<p>For example, if you have an addition system with four <code>x</code> wires, four <code>y</code> wires, and five <code>z</code> wires, you should be able to supply any four-bit number on the <code>x</code> wires, any four-bit number on the <code>y</code> numbers, and eventually find the sum of those two numbers as a five-bit number on the <code>z</code> wires. One of the many ways you could provide numbers to such a system would be to pass <code>11</code> on the <code>x</code> wires (<code>1011</code> in binary) and <code>13</code> on the <code>y</code> wires (<code>1101</code> in binary):</p>
<pre><code>x00: 1
x01: 1
x02: 0
x03: 1
y00: 1
y01: 0
y02: 1
y03: 1
</code></pre>
<p>If the system were working correctly, then after all gates are finished processing, you should find <code>24</code> (<code>11+13</code>) on the <code>z</code> wires as the five-bit binary number <code>11000</code>:</p>
<pre><code>z00: 0
z01: 0
z02: 0
z03: 1
z04: 1
</code></pre>
<p>Unfortunately, your actual system needs to add numbers with many more bits and therefore has many more wires.</p>
<p>Based on <span title="ENHANCE">forensic analysis</span> of scuff marks and scratches on the device, you can tell that there are exactly <em>four</em> pairs of gates whose output wires have been <em>swapped</em>. (A gate can only be in at most one such pair; no gate's output was swapped multiple times.)</p>
<p>For example, the system below is supposed to find the bitwise <code>AND</code> of the six-bit number on <code>x00</code> through <code>x05</code> and the six-bit number on <code>y00</code> through <code>y05</code> and then write the result as a six-bit number on <code>z00</code> through <code>z05</code>:</p>
<pre><code>x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -&gt; z05
x01 AND y01 -&gt; z02
x02 AND y02 -&gt; z01
x03 AND y03 -&gt; z03
x04 AND y04 -&gt; z04
x05 AND y05 -&gt; z00
</code></pre>
<p>However, in this example, two pairs of gates have had their output wires swapped, causing the system to produce wrong answers. The first pair of gates with swapped outputs is <code>x00 AND y00 -&gt; z05</code> and <code>x05 AND y05 -&gt; z00</code>; the second pair of gates is <code>x01 AND y01 -&gt; z02</code> and <code>x02 AND y02 -&gt; z01</code>. Correcting these two swaps results in this system that works as intended for any set of initial values on wires that start with <code>x</code> or <code>y</code>:</p>
<pre><code>x00 AND y00 -&gt; z00
x01 AND y01 -&gt; z01
x02 AND y02 -&gt; z02
x03 AND y03 -&gt; z03
x04 AND y04 -&gt; z04
x05 AND y05 -&gt; z05
</code></pre>
<p>In this example, two pairs of gates have outputs that are involved in a swap. By sorting their output wires' names and joining them with commas, the list of wires involved in swaps is <code><em>z00,z01,z02,z05</em></code>.</p>
<p>Of course, your actual system is much more complex than this, and the gates that need their outputs swapped could be <em>anywhere</em>, not just attached to a wire starting with <code>z</code>. If you were to determine that you need to swap output wires <code>aaa</code> with <code>eee</code>, <code>ooo</code> with <code>z99</code>, <code>bbb</code> with <code>ccc</code>, and <code>aoc</code> with <code>z24</code>, your answer would be <code><em>aaa,aoc,bbb,ccc,eee,ooo,z24,z99</em></code>.</p>
<p>Your system of gates and wires has <em>four</em> pairs of gates which need their output wires swapped - <em>eight</em> wires in total. Determine which four pairs of gates need their outputs swapped so that your system correctly performs addition; <em>what do you get if you sort the names of the eight wires involved in a swap and then join those names with commas?</em></p>
</article>
<p>Your puzzle answer was <code>dnt,gdf,gwc,jst,mcm,z05,z15,z30</code>.</p><p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
<p>At this point, you should <a href="/2024">return to your Advent calendar</a> and try another puzzle.</p>
<p>If you still want to see it, you can <a href="24/input" target="_blank">get your puzzle input</a>.</p>
<p>You can also <span class="share">[Share<span class="share-content">on
  <a href="https://bsky.app/intent/compose?text=I%27ve+completed+%22Crossed+Wires%22+%2D+Day+24+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F24" target="_blank">Bluesky</a>
  <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Crossed+Wires%22+%2D+Day+24+%2D+Advent+of+Code+2024&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F24&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
  <a href="javascript:void(0);" onclick="var ms; try{ms=localStorage.getItem('mastodon.server')}finally{} if(typeof ms!=='string')ms=''; ms=prompt('Mastodon Server?',ms); if(typeof ms==='string' &amp;&amp; ms.length){this.href='https://'+ms+'/share?text=I%27ve+completed+%22Crossed+Wires%22+%2D+Day+24+%2D+Advent+of+Code+2024+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2024%2Fday%2F24';try{localStorage.setItem('mastodon.server',ms);}finally{}}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
</main>