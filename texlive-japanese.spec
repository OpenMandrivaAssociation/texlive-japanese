# revision 30855
# category Package
# catalog-ctan /language/japanese/japanese
# catalog-date 2012-02-06 14:44:00 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-japanese
Version:	1.3
Release:	13
Summary:	A substitute for a babel package for Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/japanese
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package behaves in a similar way as if you provided the
(non-existent) Japanese option to babel so that you can handle
Japanese language text in LaTeX documents. The package requires
a Japanese-enabled TeX system, such as pTeX or jTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/platex/japanese/japanese.ldf
%doc %{_texmfdistdir}/doc/platex/japanese/README
%doc %{_texmfdistdir}/doc/platex/japanese/sample.pdf
%doc %{_texmfdistdir}/doc/platex/japanese/sample.tex
#- source
%doc %{_texmfdistdir}/source/platex/japanese/japanese.dtx
%doc %{_texmfdistdir}/source/platex/japanese/japanese.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
