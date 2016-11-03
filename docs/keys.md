# Key Names

## Modifier Keys

These keys act as "modifiers", in that they can be held down while other keys
are pressed.  These have a special meaning for the *hotkey* modes.  In the
override mode, they act just as any other key.

| Key on the Keyboard | Config Name(s) |
| ------------------- | -------------- |
| <kbd>&#x21e7; Shift</kbd> | `shift` (either shift key), `lshift` (left shift key), `rshift` (right shift key) |
| <kbd>&#x2756; Win</kbd> (Also called the *Super* key) | `win` (either Win key), `lwin` (left Win key), `rwin` (right win key) |
| <kbd>&#x2732; Ctrl</kbd> | `ctrl` (either Control key), `lctrl` (left Control key), `rctrl` (right Control key) |
| <kbd>Alt</kbd> | `alt` (either Alt key), `lalt` (left Alt key), `ralt` (right Alt key) |
| <kbd>&#x21ea; Caps Lock</kbd> | `caps-lock` |

## Normal Keys

These are all keys that can be used with modifiers.


### Standard Keys

The keys <kbd>A</kbd> through <kbd>Z</kbd>, and <kbd>0</kbd> through <kbd>9</kbd>
are all used in the configuration as their corresponding key name.


### Numpad Keys

The numpad keys <kbd>0</kbd> through <kbd>9</kbd> are defined in the
configuration as `numpad0` to `numpad9`.  Additionally, these other keys are
defined:

| Key on the Keyboard | Config Name(s) |
| ------------------- | -------------- |
| <kbd>Numpad *</kbd> | `multiply` |
| <kbd>Numpad +</kbd> | `add` |
| <kbd>Numpad -</kbd> | `subtract` |
| <kbd>Numpad Enter</kbd> | `separator` |
| <kbd>Numpad .</kbd> | `decimal` |
| <kbd>Numpad /</kbd> | `divide` |
| <kbd>Num Lock</kbd> | `numlock` |


### Function Keys

The function keys <kbd>F1</kbd> to <kbd>F24</kbd> (yep!) are defined in the
configuration file as `f1` to `f24`.


### Named Keys

| Key on the Keyboard | Config Name(s) |
| ------------------- | -------------- |
| <kbd>&crarr; Enter</kbd> | `enter`, `return`, `cr`, `lf` |
| <kbd>&#x25a4; Menu</kbd> | `apps` |
| <kbd>Tab &#x21b9;</kbd> | `tab` |
| <kbd>&larr;</kbd> | `left` |
| <kbd>&rarr;</kbd> | `right` |
| <kbd>&uarr;</kbd> | `up` |
| <kbd>&darr;</kbd> | `down` |
| <kbd>&#x232b; Backspace</kbd> | `backspace`, `back` |
| <kbd>Esc</kbd> | `esc`, `escape` |
| <kbd>Space bar</kbd> | `space` |
| <kbd>PgUp</kbd>, <kbd>Page Up</kbd> | `pgup`, `pageup`, `prior` |
| <kbd>PgDn</kbd>, <kbd>Page Down</kbd | `pgdn`, `pagedown`, `next` |
| <kbd>End</kbd> | `end` |
| <kbd>Home</kbd> | `home` |
| <kbd>Print Screen/SysRq</kbd> | `snapshot` |
| <kbd>Insert</kbd>, <kbd>Ins</kbd> | `insert` |
| <kbd>Delete</kbd>, <kbd>Del</kbd> | `delete`, `del` |
| <kbd>Clear</kbd> | `clear` |
| <kbd>Scroll Lock</kbd> | `scroll` |
| <kbd>&#x263e; Sleep</kbd> | `sleep` |
| <kbd>Back</kbd> | `browser-back` |
| <kbd>Forward</kbd> | `browser-forward` |
| <kbd>&#x27f2; Refresh</kbd> | `browser-refresh` |
| <kbd>Stop</kbd> | `browser-stop` |
| <kbd>Favorites</kbd> | `browser-favorites` |
| <kbd>&#x2302; Home</kbd> | `browser-home` |
| <kbd>&#x1f50e; Search</kbd> | `browser-search` |
| <kbd>&#x1f507; Mute</kbd> | `volume-mute` |
| <kbd>&#x1f508; No Volume</kbd> | `volume-off` (TODO not properly implemented; fix this) |
| <kbd>&#x1f509; Volume Down</kbd> | `volume-down` |
| <kbd>&#x1f50a; Volume Up</kbd> | `volume-up` |
| <kbd>&#x25fc; Stop</kbd> | `media-stop` |
| <kbd>&#x23ef; Play/Pause</kbd> | `media-play-pause` |
| <kbd>&#x23ee; Previous Song</kbd> |`media-prev-track` |
| <kbd>&#x23ed; Next Song</kbd> |`media-next-track` |
| <kbd>&#x2709; Mail</kbd> | `launch-mail` |
| <kbd>(select media)</kbd> | `launch-media-select` |
| <kbd>(computer)</kbd> | `launch-app-1` |
| <kbd>(calculator)</kbd> | `launch-app-2` |
| <kbd>&#x23ea; Fast Backward</kbd> | ? |
| <kbd>&#x23e9; Fast Forward</kbd> | ? |
| <kbd>&#x1f505; Lower Brightness</kbd> | ? |
| <kbd>&#x1f506; Raise Brightness</kbd> | ? |
| <kbd>:/;</kbd> | `:`, `;`, `colon` |
| <kbd>+/=</kbd> | `plus` |
| <kbd>,/&lt;</kbd> | `,`, `<`, `comma` |
| <kbd>-/_</kbd> | `minus` |
| <kbd>./&gt;</kbd> | `.`, `>`, `period` |
| <kbd>//?</kbd> | `/`, `slash`, `?`, `question`, `question-mark` |
| <kbd>\`/~</kbd> | `~`, `\`, `tilde`, `twiddle`, `back-tick` |
| <kbd>\[/{</kbd> | `[`, `{`, `left-bracket` |
| <kbd>\|/\\</kbd> | `|`, `\`, `pipe`, `backslash` |
| <kbd>]/}</kbd> | `]`, `}`, `right-bracket` |
| <kbd>'/"</kbd> | `"`, `'`, `quote`, `tick` |
    

## Others

These need to be verified

| Key on the Keyboard | Config Name(s) |
| ------------------- | -------------- |
| <kbd>Pause/Break</kbd> | `break`, `pause` (TODO see if these are actually different) |
| <kbd>半角/全角</kbd>, <kbd>한/영</kbd> | `kana`, `hangul` |
| <kbd>(unknown)</kbd> | `junja` |
| <kbd>한자</kbd> | `hanja` |
| <kbd>漢字</kbd> | `kanji` |
| <kbd>CrSel</kbd> | `crsel` |
| <kbd>ExSel</kbd> | `exsel` |
| <kbd>(unknown)</kbd> | `final` |
| <kbd>(unknown)</kbd> | `convert` |
| <kbd>(unknown)</kbd> | `nonconvert` |
| <kbd>(unknown)</kbd> | `accept` |
| <kbd>(unknown)</kbd> | `modechange` |
| <kbd>(unknown)</kbd> | `select` |
| <kbd>(unknown)</kbd> | `print` |
| <kbd>(unknown)</kbd> | `execute` |
| <kbd>(unknown)</kbd> | `help` |
| <kbd>(unknown)</kbd> | `processkey` |
| <kbd>(unknown)</kbd> | `attn` |
| <kbd>(unknown)</kbd> | `ereof` |
| <kbd>(unknown)</kbd> | `play` |
| <kbd>(unknown)</kbd> | `zoom` |
| <kbd>(unknown)</kbd> | `noname` |
| <kbd>(unknown)</kbd> | `pa1` |
