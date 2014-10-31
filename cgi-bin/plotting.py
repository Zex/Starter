#!/usr/bin/env python
#
# plotting.py
# Author: Zex <top_zlynch@yahoo.com>
#
#   rcParams {    
#    'axes.formatter.use_locale': False,
#    'figure.subplot.right': 0.9,
#    'mathtext.cal': 'cursive',
#    'font.fantasy': ['Comic Sans MS',
#    'Chicago',
#    'Charcoal',
#    'ImpactWestern',
#    'fantasy'],
#    'xtick.minor.pad': 4,
#    'tk.pythoninspect': False,
#    'image.aspect': 'equal',
#    'font.cursive': ['Apple Chancery',
#    'Textile',
#    'Zapf Chancery',
#    'Sand',
#    'cursive'],
#    'figure.subplot.hspace': 0.2,
#    'keymap.fullscreen': 'f',
#    'examples.directory': "/etc/'/usr/share/matplotlib/sampledata'",
#    'xtick.direction': 'in',
#    'axes.facecolor': 'w',
#    'mathtext.fontset': 'cm',
#    'ytick.direction': 'in',
#    'keymap.pan': 'p',
#    'path.snap': True,
#    'axes.axisbelow': False,
#    'lines.markersize': 6,
#    'figure.dpi': 80,
#    'text.usetex': False,
#    'image.origin': 'upper',
#    'patch.edgecolor': 'k',
#    'legend.labelspacing': 0.5,
#    'ps.useafm': False,
#    'mathtext.bf': 'serif:bold',
#    'text.antialiased': True,
#    'lines.solid_joinstyle': 'round',
#    'font.monospace': ['Bitstream Vera Sans Mono',
#    'DejaVu Sans Mono',
#    'Andale Mono',
#    'Nimbus Mono L',
#    'Courier New',
#    'Courier',
#    'Fixed',
#    'Terminal',
#    'monospace'],
#    'xtick.minor.size': 2,
#    'axes.formatter.limits': [-7, 7],
#    'figure.subplot.wspace': 0.2,
#    'font.serif': ['Bitstream Vera Serif',
#    'DejaVu Serif',
#    'New Century Schoolbook',
#    'Century Schoolbook L',
#    'Utopia',
#    'ITC Bookman',
#    'Bookman',
#    'Nimbus Roman No9 L',
#    'Times New Roman',
#    'Times',
#    'Palatino',
#    'Charter',
#    'serif'],
#    'image.cmap': 'jet',
#    'lines.marker': 'None',
#    'tk.window_focus': False,
#    'ytick.major.width': 0.5,
#    'backend.qt4': 'PyQt4',
#    'savefig.edgecolor': 'w',
#    'savefig.facecolor': 'w',
#    'ytick.minor.size': 2,
#    'font.stretch': 'normal',
#    'text.dvipnghack': None,
#    'ytick.color': 'k',
#    'svg.fonttype': 'path',
#    'lines.linestyle': '-',
#    'xtick.color': 'k',
#    'xtick.major.pad': 4,
#    'patch.facecolor': 'b',
#    'figure.figsize': [8.0, 6.0],
#    'axes.linewidth': 1.0,
#    'keymap.zoom': 'o',
#    'legend.handletextpad': 0.8,
#    'mathtext.fallback_to_cm': True,
#    'lines.linewidth': 1.0,
#    'savefig.dpi': 100,
#    'verbose.fileo': 'sys.stdout',
#    'svg.image_noscale': False,
#    'docstring.hardcopy': False,
#    'font.size': 12,
#    'ps.fonttype': 3,
#    'path.simplify': True,
#    'keymap.all_axes': 'a',
#    'polaraxes.grid': True,
#    'text.hinting': True,
#    'pdf.compression': 6,
#    'grid.linewidth': 0.5,
#    'legend.frameon': True,
#    'figure.autolayout': False,
#    'figure.facecolor': '0.75',
#    'xtick.minor.width': 0.5,
#    'ps.usedistiller': False,
#    'legend.isaxes': True,
#    'figure.edgecolor': 'w',
#    'mathtext.tt': 'monospace',
#    'contour.negative_linestyle': 'dashed',
#    'image.interpolation': 'bilinear',
#    'lines.markeredgewidth': 0.5,
#    'keymap.home': ['h', 'r', 'home'],
#    'axes3d.grid': True,
#    'axes.edgecolor': 'k',
#    'legend.shadow': False,
#    'ytick.minor.width': 0.5,
#    'axes.titlesize': 'large',
#    'backend': 'TkAgg',
#    'xtick.major.size': 4,
#    'keymap.xscale': ['k', 'L'],
#    'legend.fontsize': 'large',
#    'lines.solid_capstyle': 'projecting',
#    'mathtext.it': 'serif:italic',
#    'keymap.save': 's',
#    'font.variant': 'normal',
#    'toolbar': 'toolbar2',
#    'xtick.labelsize': 'medium',
#    'axes.unicode_minus': True,
#    'ps.distiller.res': 6000,
#    'axes.labelweight': 'normal',
#    'pdf.fonttype': 3,
#    'patch.linewidth': 1.0,
#    'pdf.inheritcolor': False,
#    'axes.color_cycle': ['b', 'g', 'r', 'c', 'm', 'y', 'k'],
#    'lines.dash_capstyle': 'butt',
#    'lines.color': 'b',
#    'figure.subplot.top': 0.9,
#    'pdf.use14corefonts': False,
#    'legend.markerscale': 1.0,
#    'patch.antialiased': True,
#    'font.style': 'normal',
#    'keymap.forward': ['right', 'v'],
#    'backend_fallback': True,
#    'legend.fancybox': False,
#    'grid.linestyle': ':',
#    'savefig.extension': 'auto',
#    'text.color': 'k',
#    'mathtext.rm': 'serif',
#    'legend.loc': 'upper right',
#    'interactive': False,
#    'cairo.format': 'png',
#    'savefig.orientation': 'portrait',
#    'svg.image_inline': True,
#    'ytick.major.size': 4,
#    'axes.grid': False,
#    'plugins.directory': '.matplotlib_plugins',
#    'grid.color': 'k',
#    'timezone': 'UTC',
#    'ytick.major.pad': 4,
#    'legend.borderpad': 0.4,
#    'examples.download': False,
#    'lines.dash_joinstyle': 'round',
#    'datapath': '/usr/share/matplotlib/mpl-data',
#    'lines.antialiased': True,
#    'text.latex.unicode': False,
#    'legend.handleheight': 0.7,
#    'image.lut': 256,
#    'figure.subplot.bottom': 0.1,
#    'text.latex.preamble': [''],
#    'legend.numpoints': 2,
#    'legend.handlelength': 2
#   }
from navi import *

def random_plot(begin, end, step = 1, titlestr = None):

    from pylab import plot, xlabel, ylabel, show, savefig, title
    from random import randint

    plot([randint(begin, end) for i in xrange(begin, end/3, step)],
        [randint(begin, end) for i in xrange(begin, end/3, step)],
        'r--')

    plot([randint(begin, end) for i in xrange(begin, end/3, step)],
        [randint(begin, end) for i in xrange(begin, end/3, step)],
        'g.')

    plot([randint(begin, end) for i in xrange(begin, end/3, step)],
        [randint(begin, end) for i in xrange(begin, end/3, step)],
        'mh')

    plot([randint(begin, end) for i in xrange(begin, end/3, step)],
        [randint(begin, end) for i in xrange(begin, end/3, step)],
        'k+')

    title(titlestr)
    xlabel('X')
    ylabel('Y')
#    show()
    savefig("../img/" + titlestr.replace(' ', '-').lower())

def essay_char(essay):

    from pylab import xlabel, ylabel, show, savefig, title,\
         yticks, xlim, ylim, xticks, arange, figure, barh, grid, rcParams
    from string import ascii_letters

    cnt = { x:0 for x in ascii_letters }

    for c in essay:
        if cnt.has_key(c):
            cnt[c] += 1

    titlestr = "Essay Char"
    figure(figsize=(max(cnt.values())/4, 15), dpi=60)

    rcParams['font.size'] = 17
    rcParams['text.color'] = 'c'
    rcParams['xtick.color'] = 'r'
    rcParams['ytick.color'] = 'y'
    rcParams['figure.facecolor'] = 'k'
    rcParams['figure.edgecolor'] = 'b'
    rcParams['savefig.facecolor'] = rcParams['figure.facecolor']
    rcParams['savefig.edgecolor'] = rcParams['figure.edgecolor']
    rcParams['savefig.dpi'] = rcParams['figure.dpi']

    xlim(0, max(cnt.values()*2))
    ylim(0, len(cnt)*2)

    kbuf = cnt.keys()
    kbuf.sort()

    xticks(xrange(int(xlim()[0]), int(xlim()[1]), 2), rotation=45)
    yticks(xrange(int(ylim()[0]), int(ylim()[1]), 2), kbuf, rotation=-45)

    vbuf = [cnt[c] for c in kbuf]
    grid()

    for n, w in zip(xrange(len(vbuf)+1), vbuf):
        barh(n*2, w, height=1.5, left=0, align='center')

    title(titlestr)
    xlabel('Characters Count')
    ylabel('Essay Characters')
#    show()
    savefig("../img/" + titlestr.replace(' ', '-').lower(), bbox_inches='tight', pad_inches=0)

def reply():

    title = "Plots"
    ret = "" 
    ret += "Content-Type: text/html\n\n"
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    
    ret += default_head(title)
    ret += default_navigator()
    
    ret += "<body>"
    ret += "<div class=\"content\">"

    from threading import Thread

    Thread(target=random_plot, args=(1, 317, 1, 'Molecular Random Motion xxx')).start()

    with open('../res/Licence.Sample', 'ro') as fd:
        Thread(target=essay_char, args=(fd.read(),)).start()

    ret += "<table class=\"normal\">"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">"
    ret += "<img src=\"/img/molecular-random-motion-xxx.png\">"
    ret += "</td>"
    ret += "<td class=\"normal\">"
    ret += "<img src=\"/img/molecular-random-motion-xxx.png\">"
    ret += "</td>"
    ret += "<td class=\"normal\">"
    ret += "<img src=\"/img/molecular-random-motion-xxx.png\">"
    ret += "</td>"
    ret += "</tr>"
    ret += "</table>"
    ret += "<table class=\"normal\">"
    ret += "<tr class=\"normal\">"
    ret += "<td class=\"normal\">"
    ret += "<img src=\"/img/essay-char.png\">"
    ret += "</td>"
    ret += "</tr>"
    ret += "</table>"

    ret += "</div>" 
    ret += "</body>"
    ret += "</html>"

    print ret

from os import environ

environ['MPLCONFIGDIR'] = "/tmp"

try:
    reply()
except Exception as e:
    print e
