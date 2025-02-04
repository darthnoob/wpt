# -*- coding: utf-8 -*-
import os
ccdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template = """<!DOCTYPE html>
<!-- DO NOT EDIT! This test has been generated by /conformance-checkers/tools/picture.py. -->
<meta charset=utf-8>
"""

errors = {
    # missing src on img
    "img-no-src": "<img alt>",
    "img-no-src-with-srcset": "<img srcset=x alt>",
    "img-no-src-with-picture": "<picture><img alt></picture>",
    "img-no-src-with-srcset-and-picture": "<picture><img srcset=x alt></picture>",
    "img-no-src-with-source": "<picture><source srcset=x><img alt></picture>",
    # junk content in picture
    "junk-text-before-img": "<picture>x<img src=x alt></picture>",
    "junk-text-after-img": "<picture><img src=x alt>x</picture>",
    "junk-text-before-source": "<picture>x<source srcset=x><img src=x alt></picture>",
    "junk-text-after-source": "<picture><source srcset=x>x<img src=x alt></picture>",
    "junk-br-before-img": "<picture><br><img src=x alt></picture>",
    "junk-br-after-img": "<picture><img src=x alt><br></picture>",
    "junk-br-before-source": "<picture><br><source srcset=x><img src=x alt></picture>",
    "junk-br-after-source": "<picture><source srcset=x><br><img src=x alt></picture>",
    "junk-video-before": "<picture><video></video><source srcset=x><img src=x alt></picture>",
    "junk-video-no-img": "<picture><video></video></picture>",
    "junk-p-before": "<picture><p></p><source srcset=x><img src=x alt></picture>",
    "junk-p-after": "<picture><source srcset=x><img src=x alt><p></p></picture>",
    "junk-p-wrapping": "<picture><p><source srcset=x><img src=x alt></p></picture>",
    "junk-span-before": "<picture><span></span><source srcset=x><img src=x alt></picture>",
    "junk-span-after": "<picture><source srcset=x><img src=x alt><span></span></picture>",
    "junk-span-wrapping": "<picture><span><source srcset=x><img src=x alt></span></picture>",
    "junk-picture-before": "<picture><picture><img src=x alt></picture><img src=x alt></picture>",
    "junk-picture-wrapping": "<picture><picture><img src=x alt></picture></picture>",
    "junk-figure-wrapping": "<picture><figure><img src=x alt></figure></picture>",
    "junk-input-type-hidden": "<picture><input type=hidden name=x value=x><img src=x alt></picture>",
    "junk-style-scroped": "<picture><style scroped></style><img src=x alt></picture>",
    "junk-noscript": "<picture><img src=x alt><noscript></noscript></picture>",
    "junk-noscript-after-source-no-img": "<picture><source srcset=x><noscript><img src=x alt></noscript></picture>",
    "junk-svg": "<picture><img src=x alt><svg></svg></picture>",
    "junk-svg-no-img": "<picture><svg></svg></picture>",
    "junk-math-nog-img": "<picture><math></math></picture>",
    # parents
    "parent-ul": "<ul><picture><img src=x alt></picture></ul>",
    "parent-dl": "<dl><picture><img src=x alt></picture></dl>",
    "parent-hgroup": "<hgroup><h1>x</h1><picture><img src=x alt></picture></hgroup>",
    "parent-noscript-in-head": "<noscript><picture><img src=x alt></picture></noscript>",
    "parent-rp": "<ruby>x<rp><picture><img src=x alt></picture></rp><rt>x</rt><rp>x</rp></ruby>",
    # invalid html syntax
    "html-syntax-source-end-tag": "<picture><source srcset=x></source><img src=x alt></picture>",
    "html-syntax-img-end-tag": "<picture><img src=x alt></img></picture>",
    "html-syntax-picture-no-end-tag": "<picture><img src=x alt>",
    "html-syntax-picture-slash": "<picture/><img src=x alt></picture>",
    "html-syntax-picture-slash-no-end-tag": "<picture/><img src=x alt>",
    # missing img in picture
    "missing-img-empty-picture": "<picture></picture>",
    "missing-img-only-source": "<picture><source srcset=x></picture>",
    "missing-img-only-script": "<picture><script></script></picture>",
    "missing-img-script-and-source": "<picture><script></script><source srcset=x></picture>",
    "missing-img-source-and-script": "<picture><source srcset=x><script></script></picture>",
    # multiple img in picture
    "multiple-img": "<picture><img src=x alt><img src=x alt></picture>",
    "multiple-img-with-script": "<picture><img src=x alt><script></script><img src=x alt></picture>",
    "multiple-img-with-source": "<picture><source srcset=x><img src=x alt><img src=x alt></picture>",
    "multiple-img-with-source-and-script": "<picture><source srcset=x><img src=x alt><script></script><img src=x alt></picture>",
    # source after img
    "source-after-img": "<picture><img src=x alt><source srcset=x></picture>",
    "source-before-and-after-img": "<picture><source srcset=x><img src=x alt><source srcset=x></picture>",
    # source with following sibling source element or img element with a srcset attribute
    "always-matching-source-with-following-img-srcset": "<picture><source srcset=x><img src=x srcset=x alt></picture>",
    "always-matching-source-with-following-source-srcset": "<picture><source srcset=x><source srcset=x><img src=x alt></picture>",
    "always-matching-source-with-following-source-media": "<picture><source srcset=x><source srcset=x media=screen><img src=x alt></picture>",
    "always-matching-source-with-following-source-type": "<picture><source srcset=x><source srcset=x type=image/gif><img src=x alt></picture>",
    "always-matching-source-media-empty-with-following-source-srcset": "<picture><source srcset=x media><source srcset=x><img src=x alt></picture>",
    "always-matching-source-media-spaces-with-following-source-srcset": "<picture><source srcset=x media=' \n\t'><source srcset=x><img src=x alt></picture>",
    "always-matching-source-media-all-with-following-source-srcset": "<picture><source srcset=x media=all><source srcset=x><img src=x alt></picture>",
    "always-matching-source-media-uppercase-with-following-source-srcset": "<picture><source srcset=x media=ALL><source srcset=x><img src=x alt></picture>",
    "always-matching-source-media-all-spaces-with-following-source-srcset": "<picture><source srcset=x media=' all '><source srcset=x><img src=x alt></picture>",
    "always-matching-source-sizes-with-following-source-srcset": "<picture><source srcset='x 100w' sizes=50vw><source srcset=x><img src=x alt></picture>",
    # sizes present
    "img-srcset-no-descriptor-with-sizes": "<img src=x srcset='x' sizes=50vw alt>",
    "img-srcset-w-and-x-width-sizes": "<img src=x srcset='x 100w, y 2x' sizes=50vw alt>",
    "source-srcset-x-with-sizes": "<picture><source srcset='x 1x, y 2x' sizes=50vw><img src=x alt></picture>",
    "source-srcset-h-with-sizes": "<picture><source srcset='x 100h, y 200h' sizes=50vw><img src=x alt></picture>",
    "source-srcset-w-and-x-with-sizes": "<picture><source srcset='x 100w, y 2x' sizes=50vw><img src=x alt></picture>",
    "img-with-sizes-no-srcset": "<img sizes=50vw src=foo alt>",
    # width descriptor without sizes
    "img-srcset-w-no-sizes": "<img srcset='x 100w, y 200w' src=x alt>",
    "source-srcset-w-no-sizes": "<picture><source srcset='x 100w, y 200w'><img src=x alt></picture>",
    "source-type-srcset-w": "<picture><source srcset='x 100w, y 200w' type=image/gif><img src=x alt></picture>",
    # invalid attributes on source
    "source-src": "<picture><source src=x><img src=x alt></picture>",
    "source-src-srcset": "<picture><source src=x srcset=x><img src=x alt></picture>",
    "source-alt": "<picture><source srcset=x alt><img src=x alt></picture>",
    "source-width": "<picture><source srcset=x width=100><img src=x alt></picture>",
    "source-height": "<picture><source srcset=x height=100><img src=x alt></picture>",
    "source-usemap": "<picture><source srcset=x usemap><img src=x alt></picture>",
    "source-ismap": "<picture><source srcset=x ismap><img src=x alt></picture>",
    "source-crossorigin": "<picture><source srcset=x crossorigin><img src=x alt></picture>",
    "source-name": "<picture><source srcset=x crossorigin><img src=x alt></picture>",
    "source-align": "<picture><source srcset=x align=left><img src=x alt></picture>",
    "source-hspace": "<picture><source srcset=x hspace=1><img src=x alt></picture>",
    "source-vspace": "<picture><source srcset=x vspace=1><img src=x alt></picture>",
    "source-longdesc": "<picture><source srcset=x longdesc=x><img src=x alt></picture>",
    "source-border": "<picture><source srcset=x border=1><img src=x alt></picture>",
    # missing srcset on source
    "source-no-srcset": "<picture><source><img src=x alt></picture>",
    "source-no-srcset-with-sizes": "<picture><source sizes=50vw><img src=x alt></picture>",
    "source-no-srcset-with-media": "<picture><source media=screen><img src=x alt></picture>",
    "source-no-srcset-with-type": "<picture><source type='image/webp'><img src=x alt></picture>",
    # invalid attributes on picture
    "picture-src": "<picture src=x><img src=x alt></picture>",
    "picture-srcset": "<picture srcset=x><img src=x alt></picture>",
    "picture-media": "<picture media=screen><img src=x alt></picture>",
    "picture-sizes": "<picture sizes=50vw><img src=x alt></picture>",
    "picture-alt": "<picture alt><img src=x alt></picture>",
    "picture-width": "<picture width=100><img src=x alt></picture>",
    "picture-height": "<picture height=100><img src=x alt></picture>",
    "picture-usemap": "<picture usemap><img src=x alt></picture>",
    "picture-ismap": "<picture ismap><img src=x alt></picture>",
    "picture-crossorigin": "<picture crossorigin><img src=x alt></picture>",
    "picture-name": "<picture name=x><img src=x alt></picture>",
    "picture-lowsrc": "<picture lowsrc=x><img src=x alt></picture>",
    "picture-align": "<picture align=left><img src=x alt></picture>",
    "picture-hspace": "<picture hspace=1><img src=x alt></picture>",
    "picture-vspace": "<picture vspace=1><img src=x alt></picture>",
    "picture-longdesc": "<picture longdesc=x><img src=x alt></picture>",
    "picture-border": "<picture border=1><img src=x alt></picture>",
    # invalid attributes on source in video
    "video-source-srcset": "<video><source srcset=x></video>",
    "video-source-srcset-src": "<video><source srcset=x src=x></video>",
    "video-source-sizes-srcset": "<video><source sizes=50vw srcset='x 100w'></video>",
    "video-source-media-src": "<video><source media=screen src=x></video>",
    # srcset on other elements
    "link-rel-icon-srcset": "<link rel=icon srcset=x href=x>",
    "input-type-image-srcset": "<input type=image src=x srcset=x alt=x>",
    "object-srcset": "<object data=x srcset=x></object>",
    "video-srcset": "<video src=x srcset=x></video>",
    "audio-srcset": "<audio src=x srcset=x></audio>",
    "track-srcset": "<video src=x><track src=x srcset=x></video>",
    "svg-image-srcset": "<svg><image xlink:href=x srcset=x width=1 height=1 /></svg>",
    # invalid attributes on img
    "img-type": "<img src=x type=image/gif alt>",
    "img-type-with-picture": "<picture><img src=x type=image/gif alt></picture>",
    # sizes microsyntax
    "sizes-microsyntax-media-all": "<img sizes='all 500px, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-media-all-and-min-width": "<img sizes='all and (min-width:500px) 500px, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-media-min-width-no-parenthesis": "<img sizes='min-width:500px 500px, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-media-general-enclosed-junk": "<img sizes='(123) 500px, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-media-bad-junk": "<img sizes='(}) 500px, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-two-defaults": "<img sizes='500px, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-default-first": "<img sizes='100vw, (min-width:500px) 500px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-trailing-comma": "<img sizes='(min-width:500px) 500px, 100vw,' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-trailing-junk": "<img sizes='(min-width:500px) 500px, 100vw, foo bar' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-junk-in-default": "<img sizes='(min-width:500px) 500px, 100vw foo bar' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-junk-in-source-size": "<img sizes='(min-width:500px) 500px foo bar, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-percent-in-source-size-value": "<img sizes='(min-width:500px) 50%, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-no-unit-in-source-size-value": "<img sizes='(min-width:500px) 50, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-deg-source-size-value": "<img sizes='1deg' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-grad-source-size-value": "<img sizes='1grad' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-rad-source-size-value": "<img sizes='1rad' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-turn-source-size-value": "<img sizes='1turn' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-s-source-size-value": "<img sizes='1s' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-ms-source-size-value": "<img sizes='1ms' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-hz-source-size-value": "<img sizes='1Hz' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-khz-source-size-value": "<img sizes='1kHz' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-dpi-source-size-value": "<img sizes='1dpi' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-dpcm-source-size-value": "<img sizes='1dpcm' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-dppx-source-size-value": "<img sizes='1dppx' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-auto-source-size-value": "<img sizes='auto' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-inherit-source-size-value": "<img sizes='inherit' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-initial-source-size-value": "<img sizes='initial' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-default-source-size-value": "<img sizes='default' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-foo-bar-source-size-value": "<img sizes='foo-bar' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-negative-source-size-value": "<img sizes='-1px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-empty": "<img sizes='' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-comma": "<img sizes=',' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-css-comment-after-plus": "<img sizes='+/**/50vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-css-comment-before-unit": "<img sizes='50/**/vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-scientific-notation-negative": "<img sizes='-1e+0px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-scientific-notation-non-integer-in-exponent": "<img sizes='1e+1.5px' srcset='x 100w, y 200w' src=x alt>",
    # srcset microsyntax
    "srcset-microsyntax-leading-comma": "<img srcset=',x' src=x alt>",
    "srcset-microsyntax-leading-comma-multiple": "<img srcset=',,,x' src=x alt>",
    "srcset-microsyntax-trailing-comma": "<img srcset='x,' src=x alt>",
    "srcset-microsyntax-trailing-comma-multiple": "<img srcset='x,,,' src=x alt>",
    "srcset-microsyntax-broken-url": "<img srcset='http: 1x' src=x alt>",
    "srcset-microsyntax-non-integer-w": "<img srcset='x 1.5w' sizes=100vw src=x alt>",
    "srcset-microsyntax-uppercase-w": "<img srcset='x 1W' sizes=100vw src=x alt>",
    "srcset-microsyntax-plus-w": "<img srcset='x +1w' sizes=100vw src=x alt>",
    "srcset-microsyntax-scientific-notation-w": "<img srcset='x 1e0w' sizes=100vw src=x alt>",
    "srcset-microsyntax-zero-w": "<img srcset='x 0w' sizes=100vw src=x alt>",
    "srcset-microsyntax-negative-zero-w": "<img srcset='x -0w' sizes=100vw src=x alt>",
    "srcset-microsyntax-negative-w": "<img srcset='x -1w' sizes=100vw src=x alt>",
    "srcset-microsyntax-plus-x": "<img srcset='x +1x' src=x alt>",
    "srcset-microsyntax-negative-x": "<img srcset='x -1x' src=x alt>",
    "srcset-microsyntax-zero-x": "<img srcset='x 0x' src=x alt>",
    "srcset-microsyntax-negative-zero-x": "<img srcset='x -0x' src=x alt>",
    "srcset-microsyntax-leading-dot-x": "<img srcset='x .5x' src=x alt>",
    "srcset-microsyntax-nan-x": "<img srcset='x NaNx' src=x alt>",
    "srcset-microsyntax-infinity-x": "<img srcset='x Infinityx' src=x alt>",
    "srcset-microsyntax-x-and-w": "<img srcset='x 1x 1w' sizes=100vw src=x alt>",
    "srcset-microsyntax-x-and-h": "<img srcset='x 1x 1h' sizes=100vw src=x alt>",
    "srcset-microsyntax-w-and-h": "<img srcset='x 1w 1h' sizes=100vw src=x alt>",
    "srcset-microsyntax-h": "<img srcset='x 1h' sizes=100vw src=x alt>",
    "srcset-microsyntax-function": "<img srcset='x foobar(baz quux, lol), y 1x' src=x alt>",
    "srcset-microsyntax-parenthesis-junk": "<img srcset='x ><(((((o)>, y 1x' src=x alt>",
    "srcset-microsyntax-square-bracket-junk": "<img srcset='x [, y 1x' src=x alt>",
    "srcset-microsyntax-curly-bracket-junk": "<img srcset='x {, y 1x' src=x alt>",
    "srcset-microsyntax-pipe-junk": "<img srcset='x ||, y 1x' src=x alt>",
    "srcset-microsyntax-w-and-no-descriptor": "<img srcset='x 1w, y' sizes=100vw src=x alt>",
    "srcset-microsyntax-unique-descriptors-1x-and-omitted": "<img srcset='x 1x, y' src=x alt>",
    "srcset-microsyntax-unique-descriptors-2x": "<img srcset='x 2x, y 2x' src=x alt>",
    "srcset-microsyntax-unique-descriptors-integer-and-decimals-x": "<img srcset='x 1x, y 1.0x' src=x alt>",
    "srcset-microsyntax-unique-descriptors-w": "<img srcset='x 1w, y 1w' sizes=100vw src=x alt>",
    "srcset-microsyntax-empty": "<img srcset='' src=x alt>",
    "srcset-microsyntax-comma": "<img srcset=',' src=x alt>",
    "srcset-microsyntax-css-comment-after-descriptor": "<img srcset='x 2x/**/' src=x alt>",
    # aria
    "picture-aria-role-img": "<picture role=img><img src=x alt></picture>",
    "picture-aria-role-button": "<picture role=button><img src=x alt></picture>",
    "picture-aria-role-region": "<picture role=region><img src=x alt></picture>",
    "picture-aria-role-application": "<picture role=application><img src=x alt></picture>",
    "source-aria-role-img": "<picture><source role=img srcset=x><img src=x alt></picture>",
    "picture-aria-role-presentation": "<picture role=presentation><img src=x alt></picture>",
    "source-aria-role-presentation": "<picture><source role=presentation srcset=x><img src=x alt></picture>",
}

non_errors_in_head = {
    "parent-template-in-head": "<template><picture><img src=x alt></picture></template>",
}

non_errors = {
    # basic
    "basic-img-src": "<img src=x alt>",
    "basic-picture-img-src": "<picture><img src=x alt></picture>",
    "basic-picture-source": "<picture><source srcset=x><img src=x alt></picture>",
    # inter-element whitespace
    "inter-element-whitespace": "<picture> <!--x--> <source srcset=x> <!--x--> <img src=x alt> <!--x--> </picture>",
    # parents
    "parent-p": "<p><picture><img src=x alt></picture></p>",
    "parent-h1": "<h1><picture><img src=x alt=x></picture></h1>",
    "parent-noscript-in-body": "<noscript><picture><img src=x alt></picture></noscript>",
    "parent-object": "<object data=x><picture><img src=x alt></picture></object>",
    "parent-video": "<video src=x><picture><img src=x alt></picture></video>",
    "parent-section": "<section><h2>x</h2><picture><img src=x alt></picture></section>",
    "parent-main": "<main><picture><img src=x alt></picture></main>",
    "parent-canvas": "<canvas><picture><img src=x alt></picture></canvas>",
    "parent-template-in-body": "<template><picture><img src=x alt></picture></template>",
    "parent-ruby": "<ruby><picture><img src=x alt></picture><rt>x</rt></ruby>",
    "parent-rt": "<ruby>x<rt><picture><img src=x alt></picture></rt></ruby>",
    "parent-a": "<a href=x><picture><img src=x alt></picture></a>",
    "parent-button": "<button><picture><img src=x alt></picture></button>",
    "parent-td": "<table><tr><td><picture><img src=x alt></picture></table>",
    # script-supporting elements
    "script-first": "<picture><script></script><source srcset=x><img src=x alt></picture>",
    "template-first": "<picture><template></template><source srcset=x><img src=x alt></picture>",
    "script-between": "<picture><source srcset=x><script></script><img src=x alt></picture>",
    "script-after": "<picture><source srcset=x><img src=x alt><script></script></picture>",
    "script-before-after": "<picture><script></script><source srcset=x><img src=x alt><script></script></picture>",
    "script-before-between-after": "<picture><script></script><source srcset=x><script></script><img src=x alt><script></script></picture>",
    "script-and-template": "<picture><template></template><source srcset=x><script></script><img src=x alt><template></template></picture>",
    # source with following sibling source element or img element with a srcset attribute
    "source-with-media-img-with-srcset": "<picture><source srcset=x media=screen><img src=x srcset=x alt></picture>",
    "source-with-media-uppercase-img-with-srcset": "<picture><source srcset=x media=SCREEN><img src=x srcset=x alt></picture>",
    "source-with-media-spaces-img-with-srcset": "<picture><source srcset=x media=' \n\tscreen \n\t'><img src=x srcset=x alt></picture>",
    "source-with-media-source-with-srcset": "<picture><source srcset=x media=screen><source srcset=x><img src=x alt></picture>",
    "source-with-type-img-with-srcset": "<picture><source srcset=x type=image/gif><img src=x srcset=x alt></picture>",
    "source-with-type-source-with-srcset": "<picture><source srcset=x type=image/gif><source srcset=x><img src=x alt></picture>",
    # sizes present
    "img-with-sizes": "<img srcset='x 100w, y 200w' sizes=50vw src=x alt>",
    "source-with-sizes": "<picture><source srcset='x 100w, y 200w' sizes=50vw><img src=x alt></picture>",
    # embed allows any attributes
    "embed-srcset-empty": "<embed srcset>",
    "embed-srcset-junk": "<embed srcset='foo bar'>",
    "embed-sizes-empty": "<embed sizes>",
    "embed-sizes-junk": "<embed sizes='foo bar'>",
    # img src also in srcset
    "img-src-also-in-srcset-1x": "<img src=x srcset='x 1x, y 2x' alt>",
    "img-src-also-in-srcset-2x": "<img src=x srcset='y 1x, x 2x' alt>",
    "img-src-also-in-srcset-w": "<img src=x srcset='x 100w, y 200w' sizes=100vw alt>",
    # img src not in srcset
    "img-src-not-in-srcset-x": "<img src=x srcset='y 1x, z 2x' alt>",
    "img-src-not-in-srcset-w": "<img src=x srcset='y 100w, z 200w' sizes=100vw alt>",
    # source type
    "source-type": "<picture><source srcset=x type=image/gif><img src=x alt></picture>",
    "source-type-srcset-x": "<picture><source srcset='x 1x, y 2x' type=image/gif><img src=x alt></picture>",
    "source-type-srcset-w-sizes": "<picture><source srcset='x 100w, y 200w' type=image/gif sizes=50vw><img src=x alt></picture>",
    # sizes microsyntax
    "sizes-microsyntax-media-min-width": "<img sizes='(min-width:500px) 500px, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-multiple-source-sizes": "<img sizes='(min-width:1500px) 500px, (min-width:1000px) 33vw, (min-width:500px) 50vw, 100vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-no-default": "<img sizes='(min-width:500px) 500px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-media-not-and": "<img sizes='(not (width:500px)) and (width:500px) 500px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-only-default": "<img sizes='500px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-calc-in-default": "<img sizes='calc(500px)' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-calc-in-source-size-value": "<img sizes='(min-width:500px) calc(500px)' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-calc-in-media": "<img sizes='(min-width:calc(500px)) 500px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-zero": "<img sizes='0' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-minus-zero": "<img sizes='-0' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-em-in-source-size-value": "<img sizes='1em' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-ex-in-source-size-value": "<img sizes='1ex' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-ch-in-source-size-value": "<img sizes='1ch' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-rem-in-source-size-value": "<img sizes='1rem' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-vw-in-source-size-value": "<img sizes='1vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-vh-in-source-size-value": "<img sizes='1vh' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-vmin-in-source-size-value": "<img sizes='1vmin' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-vmax-in-source-size-value": "<img sizes='1vmax' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-cm-in-source-size-value": "<img sizes='1cm' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-mm-in-source-size-value": "<img sizes='1mm' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-q-in-source-size-value": "<img sizes='1q' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-in-in-source-size-value": "<img sizes='1in' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-pc-in-source-size-value": "<img sizes='1pc' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-pt-in-source-size-value": "<img sizes='1pt' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-px-in-source-size-value": "<img sizes='1px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-non-integer-px-in-source-size-value": "<img sizes='0.2px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-leading-css-comment": "<img sizes='/**/50vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-trailing-css-comment": "<img sizes='50vw/**/' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-plus": "<img sizes='+50vw' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-non-integer-omitted-zero": "<img sizes='.2px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-scientifi-notation-0": "<img sizes='-0e-0px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-scientifi-notation-1": "<img sizes='+11.11e+11px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-scientifi-notation-2": "<img sizes='2.2e2px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-scientifi-notation-3": "<img sizes='33E33px' srcset='x 100w, y 200w' src=x alt>",
    "sizes-microsyntax-scientifi-notation-4": "<img sizes='.4E4px' srcset='x 100w, y 200w' src=x alt>",
    # srcset microsyntax
    "srcset-microsyntax-comma-in-url": "<img srcset='x,x' src=x alt>",
    "srcset-microsyntax-percent-escaped-leading-comma-in-url": "<img srcset='%2Cx' src=x alt>",
    "srcset-microsyntax-percent-escaped-trailing-comma-in-url": "<img srcset='x%2C' src=x alt>",
    "srcset-microsyntax-percent-escaped-space-in-url": "<img srcset='%20' src=x alt>",
    "srcset-microsyntax-w": "<img srcset='x 1w' sizes=100vw src=x alt>",
    "srcset-microsyntax-x": "<img srcset='x 1x' src=x alt>",
    "srcset-microsyntax-non-integer-x": "<img srcset='x 1.5x' src=x alt>",
    "srcset-microsyntax-scientific-notation-x": "<img srcset='x 1e0x' src=x alt>",
    "srcset-microsyntax-scientific-notation-decimals-x": "<img srcset='x 1.5e0x' src=x alt>",
    "srcset-microsyntax-scientific-notation-e-plus-x": "<img srcset='x 1e+0x' src=x alt>",
    "srcset-microsyntax-scientific-notation-e-minus-x": "<img srcset='x 1e-0x' src=x alt>",
    "srcset-microsyntax-scientific-notation-e-uppercase-x": "<img srcset='x 1E0x' src=x alt>",
    "srcset-microsyntax-no-space-between-candidates": "<img srcset='x 1x,y 2x' src=x alt>",
    # valid attributes on img in picture
    "img-crossorigin-with-picture": "<picture><img crossorigin src=x alt></picture>",
    "img-usemap-with-picture": "<picture><img usemap=#x src=x alt></picture><map name=x></map>",
    "img-ismap-with-picture": "<a href=x><picture><img ismap src=x alt></picture></a>",
    "img-width-height-with-picture": "<picture><img src=x alt width=1 height=1></picture>",
    "img-width-height-zero-with-picture": "<picture><img src=x alt width=0 height=0></picture>",
    # global attributes on picture
    "picture-global-attributes": "<picture title=x class=x dir=ltr hidden id=asdf tabindex=0><img src=x alt></picture>",
}

for key in errors.keys():
    template_error = template
    template_error += '<title>invalid %s</title>\n' % key
    template_error += errors[key]
    file = open(os.path.join(ccdir, "html/elements/picture/%s-novalid.html" % key), 'wb')
    file.write(template_error)
    file.close()

file = open(os.path.join(ccdir, "html/elements/picture/picture-isvalid.html"), 'wb')
file.write(template + '<title>valid picture</title>\n')
for key in non_errors_in_head.keys():
    file.write('%s <!-- %s -->\n' % (non_errors_in_head[key], key))
file.write('<body>\n')
for key in non_errors.keys():
    file.write('%s <!-- %s -->\n' % (non_errors[key], key))
file.close()
# vim: ts=4:sw=4
