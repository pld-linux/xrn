Summary:	An X Window System based news reader
Summary(cs.UTF-8):   Jednoduchý Newsový klient pro X Window System
Summary(da.UTF-8):   En X-vinduessystembaseret nyhedslæser
Summary(de.UTF-8):   Ein Newsreader für das X Window System
Summary(es.UTF-8):   Lector de noticias para X Window
Summary(fr.UTF-8):   Lecteur de nouvelles Usenet pour le système X Window
Summary(id.UTF-8):   News reader yang berbasiskan X Window System
Summary(is.UTF-8):   Fréttalesari fyrir X gluggakerfið
Summary(it.UTF-8):   Un news reader basato su X Window
Summary(ja.UTF-8):   X Window System ベースのニュースリーダー
Summary(ko.UTF-8):   X 윈도우 시스템 기반 뉴스 읽기 프로그램
Summary(nb.UTF-8):   En nyhetsleser for X
Summary(pl.UTF-8):   Czytnik newsów pod X Window System
Summary(pt.UTF-8):   Um leitor de 'news' baseado no X Window System
Summary(ru.UTF-8):   Программа для чтения новостей в X Window System
Summary(sk.UTF-8):   Program na čítanie diskusných skupín pre systém X Window
Summary(sl.UTF-8):   Bralnik novi za Okna X
Summary(sv.UTF-8):   En nyhetsläsare för X11
Summary(zh_CN.UTF-8):   一个基于 X 窗口系统的新闻阅读器。
Name:		xrn
Version:	9.02
Release:	14
License:	distributable
Group:		Applications/News
Source0:	ftp://sipb.mit.edu/pub/xrn/%{name}-%{version}.tgz
# Source0-md5:	2920543df71c29fda8bb384a7c4f208b
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-pld.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-time.patch
URL:		http://www.mit.edu/people/jik/software/xrn.html
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	 	_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
A simple Usenet News reader for the X Window System. xrn allows you to
point and click your way through reading, replying and posting news
messages.

%description -l cs.UTF-8
xrn je jednoduchý klient pro čtení Usenet News v prostředí X Window System.

%description -l da.UTF-8
xrn er et simpelt nyhedsprogram for X.

%description -l de.UTF-8
xrn ist ein einfacher Usenet News reader für das X Window System.

%description -l es.UTF-8
xrn es un lector sencillo de noticias USENET para X Window.

%description -l fr.UTF-8
xrn est un lecteur de nouvelles Usenet simple pour le système
X Window.

%description -l it.UTF-8
xrn è un news reader di Usenet per X Window.

%description -l ja.UTF-8
xrn は X Window System 用のシンプルな Usenet ニュースリーダです。

%description -l nb.UTF-8
xrn er et enkelt newsprogram for X.

%description -l pl.UTF-8
xrn to prosty czytnik news dla X Window System. xrn pozwala na
czytanie artykułów, odpowiadanie na nie i wysyłanie nowych przy pomocy
myszki.

%description -l pt.UTF-8
O xrn é um leitor simples de 'news' da Usenet para o X Window System.

%description -l ru.UTF-8
Программа для чтения новостей в X Window System.

%description -l zh_CN.UTF-8
xrn 是一个用于 X 窗口系统的简单的 Usenet 新闻阅读器。.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xrn.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xrn.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT COMMON-PROBLMS README README.Linux TODO ChangeLog
%attr(755,root,root) %{_bindir}/xrn
%{_appdefsdir}/XRn
%{_desktopdir}/xrn.desktop
%{_pixmapsdir}/xrn.png
%{_mandir}/man1/*
