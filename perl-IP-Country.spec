#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IP
%define	pnam	Country
Summary:	IP::Country - fast lookup of country codes from IP addresses
Summary(pl.UTF-8):	IP::Country - szybkie określanie kodów państw na podstawie adresu IP
Name:		perl-IP-Country
Version:	2.26
Release:	1
# "same as perl" but read pod, some parts are licensed by APNIC/LARNIC/ARIN/AFRNIC/RIPE databases
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/N/NW/NWETTERS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1e73ba39325d197627e16de024afae82
URL:		http://search.cpan.org/dist/IP-Country/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Geography-Countries
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Finding the home country of a client using only the IP address can be
difficult. Looking up the domain name associated with that address can
provide some help, but many IP address are not reverse mapped to any
useful domain, and the most common domain (.com) offers no help when
looking for country.

This module comes bundled with a database of countries where various
IP addresses have been assigned. Although the country of assignment
will probably be the country associated with a large ISP rather than
the client herself, this is probably good enough for most log analysis
applications, and under test has proved to be as accurate as
reverse-DNS and WHOIS lookup.

%description -l pl.UTF-8
Określanie kraju pochodzenia klienta przy użyciu samego adresu IP może
być trudne. Sprawdzanie nazwy domeny związanej z adresem może być
trochę pomocne, ale wiele adresów IP nie mają odwrotnego odwzorowania
na żadną użyteczną domenę, a najpopularniejsza domena (.com) nie
pomaga w określeniu kraju.

Ten moduł jest dostarczany wraz z bazą danych krajów, do których
przypisano różne adresy IP. Choć kraj przypisania będzie
prawdopodobnie krajem związanym raczej z dużym ISP niż samym klientem,
jest to zwykle wystarczające do większości analiz logów aplikacji, a
testy dowiodły, że jest to tak samo dokładne, jak odwzorowania
odwrotnego DNS i WHOIS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README
%attr(755,root,root) %{_bindir}/ip2cc
%dir %{perl_vendorlib}/IP
%{perl_vendorlib}/IP/*.pm
%{perl_vendorlib}/IP/._Authority.pm
%{perl_vendorlib}/IP/Authority
%{perl_vendorlib}/IP/Country
%{_mandir}/man1/*
%{_mandir}/man3/*
