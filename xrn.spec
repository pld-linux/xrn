Summary:	An X Window System based news reader
Summary(pl):	Czytnik newsów pod X Window System
Name:		xrn
Version:	9.02
Release:	3
Copyright:	Distributable
Group:		Applications/News
Group(de):	Applikationen/News
Group(pl):	Aplikacje/News
Source0:	ftp://sipb.mit.edu/pub/%{name}/%{name}-%{version}.tgz
URL:		http://www.mit.edu/people/jik/software/xrn.html
Patch0:		%{name}-pld.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-time.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
A simple Usenet News reader for the X Window System. Xrn allows you to
point and click your way through reading, replying and posting news
messages.

%description -l pl
Xrn to prosty czytnik news dla X Window System. Xrn pozwala ci na
czytanie artyku³ów, odpowiadanie na nie i wysy³anie nowych przy pomocy
myszki.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf -a
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xrn <<EOF
xrn name "xrn"
xrn description "X News Reader"
xrn group Utilities/News
xrn exec "xrn &"
EOF

gzip -9nf COPYRIGHT COMMON-PROBLMS README README.Linux TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xrn
%config %{_libdir}/X11/app-defaults/XRn
%config %{_sysconfdir}/X11/wmconfig/xrn
%doc *.gz
