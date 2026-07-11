%global tl_name collection-latex
%global tl_revision 78733

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX fundamental packages
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-latex
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-latex.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(ae)
Requires:	texlive(amscls)
Requires:	texlive(amsmath)
Requires:	texlive(atbegshi)
Requires:	texlive(atveryend)
Requires:	texlive(auxhook)
Requires:	texlive(babel)
Requires:	texlive(babel-english)
Requires:	texlive(babelbib)
Requires:	texlive(bigintcalc)
Requires:	texlive(bitset)
Requires:	texlive(bookmark)
Requires:	texlive(carlisle)
Requires:	texlive(collection-basic)
Requires:	texlive(colortbl)
Requires:	texlive(epstopdf-pkg)
Requires:	texlive(etexcmds)
Requires:	texlive(etoolbox)
Requires:	texlive(fancyhdr)
Requires:	texlive(firstaid)
Requires:	texlive(fix2col)
Requires:	texlive(geometry)
Requires:	texlive(gettitlestring)
Requires:	texlive(graphics)
Requires:	texlive(graphics-cfg)
Requires:	texlive(grfext)
Requires:	texlive(hopatch)
Requires:	texlive(hycolor)
Requires:	texlive(hypcap)
Requires:	texlive(hyperref)
Requires:	texlive(intcalc)
Requires:	texlive(kvdefinekeys)
Requires:	texlive(kvoptions)
Requires:	texlive(kvsetkeys)
Requires:	texlive(l3backend)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Requires:	texlive(latex)
Requires:	texlive(latex-bin)
Requires:	texlive(latex-fonts)
Requires:	texlive(latex-lab)
Requires:	texlive(latexconfig)
Requires:	texlive(letltxmacro)
Requires:	texlive(ltxcmds)
Requires:	texlive(ltxmisc)
Requires:	texlive(lua-uni-algos)
Requires:	texlive(mfnfss)
Requires:	texlive(mptopdf)
Requires:	texlive(natbib)
Requires:	texlive(oberdiek)
Requires:	texlive(pagesel)
Requires:	texlive(pdfescape)
Requires:	texlive(pdfmanagement)
Requires:	texlive(pdftexcmds)
Requires:	texlive(pslatex)
Requires:	texlive(psnfss)
Requires:	texlive(pspicture)
Requires:	texlive(refcount)
Requires:	texlive(rerunfilecheck)
Requires:	texlive(stringenc)
Requires:	texlive(tagpdf)
Requires:	texlive(tools)
Requires:	texlive(uniquecounter)
Requires:	texlive(url)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These packages are either mandated by the core LaTeX team, or very
widely used and strongly recommended in practice.

