Summary:	Exim SpamAssassin at SMTP time
Summary(pl):	SpamAssassin dla Exima dzia³aj±cy w czasie SMTP
Name:		sa-exim
Version:	4.2
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://marc.merlins.org/linux/exim/files/%{name}-%{version}.tar.gz
URL:		http://marc.merlins.org/linux/exim/sa.html
BuildRequires:	exim-devel
Requires:	exim >= 2:4.52-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exim SpamAssassin at SMTP time.

%description -l pl
SpamAssassin dla Exima dzia³aj±cy w czasie SMTP.

%prep
%setup -q

%build
%{__make} \
	SACONF="/etc/mail/sa-exim.conf" \
	EXIM_SRC_LOCAL="%{_includedir}/exim" \
	EXIM_SRC="%{_includedir}/exim" \
	LDFLAGS="-shared -fPIC %{rpmldflags}" \
	CC="%{__cc}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/mail,%{_libdir}/exim}

install sa-exim-*.so $RPM_BUILD_ROOT%{_libdir}/exim/%{name}.so
install sa-exim.conf $RPM_BUILD_ROOT%{_sysconfdir}/mail/sa-exim.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc contrib/*.txt ACKNOWLEDGEMENTS CHANGELOG README* TODO
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/sa-exim.conf
%attr(755,root,root) %{_libdir}/exim/%{name}.so
