package com.auctionapp.auction.modules.auction;

import com.auctionapp.auction.modules.AES;
import com.auctionapp.auction.modules.auction.entity.Auction;
import com.auctionapp.auction.modules.bidder.BidderRepository;
import com.auctionapp.auction.modules.bidder.BidderService;
import com.auctionapp.auction.modules.bidder.entity.Bidder;
import com.auctionapp.auction.modules.item.ItemRepository;
import com.auctionapp.auction.modules.item.entity.Item;
import com.auctionapp.auction.modules.pairs.PairsRepository;
import com.auctionapp.auction.modules.pairs.entity.Pairs;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.io.FileWriter;
import java.io.IOException;
import java.math.BigInteger;
import java.util.*;

@Service
@RequiredArgsConstructor

public class AuctionService {
    private final AuctionRepository auctionRepository;
    private final BidderRepository bidderRepository;
    private final ItemRepository itemRepository;
    private final PairsRepository pairsRepository;
    private final BidderService bidderService;
    static AES aes = new AES();

    ResponseEntity<?> addAuction(Map<String, String> auction) {
        int idItem = Integer.parseInt(auction.get("item"));
        Item item = itemRepository.findById(idItem).orElseThrow();
        if (item.isBeingAuctioned() || item.isHasBeenSold()) {
            return new ResponseEntity<>("This item cannot be added to auction", HttpStatus.FORBIDDEN);
        } else {
            item.setBeingAuctioned(true);
            return new ResponseEntity<>(auctionRepository.save(new Auction(item)), HttpStatus.OK);
        }
    }

    ResponseEntity<?> getAuction(int id) {
        try {
            Auction auction = auctionRepository.findById(id).orElseThrow();
            return new ResponseEntity<>(auction, HttpStatus.OK);
        } catch (NoSuchElementException e) {
            return new ResponseEntity<>("There is no such auction with ID: " + id, HttpStatus.NOT_FOUND);
        }
    }

    Iterable<Auction> getAllAuctions() {
        return auctionRepository.findAll();
    }

    ResponseEntity<String> deleteAuction(int id) {
        try {
            Auction auction = auctionRepository.findById(id).orElseThrow();
            auction.item.setBeingAuctioned(false);
            List<Integer> ids = auction.biddersIds;
            if (ids.size() > 0) {
                for (int i : ids) {
                    Bidder bidder = bidderRepository.findById(i).orElseThrow();
                    bidder.setInAuction(false);
                    bidder.setValueOfBid("");
                    bidder.setWonMillionaireProblemCount(0);
                    bidderRepository.save(bidder);
                }
            }
            auctionRepository.deleteById(id);

            return new ResponseEntity<>("Auction with ID: " + id + " was deleted", HttpStatus.OK);
        } catch (NoSuchElementException e) {
            return new ResponseEntity<>("Auction with ID: " + id + " doesn't exist", HttpStatus.FORBIDDEN);
        }
    }

    ResponseEntity<?> addBidder(int auctionId, int bidderId) {
        try {
            Auction auction = auctionRepository.findById(auctionId).orElseThrow();
            Bidder bidder = bidderRepository.findById(bidderId).orElseThrow();
            if (bidder.isInAuction()) {
                return new ResponseEntity<>("Selected bidder is already in auction", HttpStatus.FORBIDDEN);
            } else if (auction.getAuctionersNumber() >= 5) {
                return new ResponseEntity<>("Auction is overloaded", HttpStatus.FORBIDDEN);
            }
            else if (auction.isHasBeenFinished()) {
                return new ResponseEntity<>("Auction is already finished", HttpStatus.FORBIDDEN);
            }
            else {
                auction.auctionersNumber++;
                auction.biddersIds.add(bidderId);
                bidder.setInAuction(true);
                auctionRepository.save(auction);
                bidderRepository.save(bidder);
                return new ResponseEntity<String>("successfully added bidder with name: " + bidder.getFirstName() + " to auction with ID: " + auction.getAuctionId(), HttpStatus.OK);
            }

        } catch (NoSuchElementException e) {
            return new ResponseEntity<>("Bidder or auction doesn't exist!", HttpStatus.FORBIDDEN);
        }
    }

    ResponseEntity<?> getAllBiddersFromChosenAuction(int auctionId) {
        try {
            Auction auction = auctionRepository.findById(auctionId).orElseThrow();
            List<Integer> ids = auction.getBiddersIds();
            List<Bidder> list = new ArrayList<>();
            if (auction.biddersIds.size() == 0) {
                return new ResponseEntity<>("Currently this auction has no bidders", HttpStatus.FORBIDDEN);
            }
            for (int i : ids) {
                Bidder bidder = bidderRepository.findById(i).orElseThrow();
                bidder.setValueOfBid(AES.decrypt(bidder.getValueOfBid(), bidder.getSurname()));
                list.add(bidder);
            }
            return new ResponseEntity<>(list, HttpStatus.OK);

        } catch (NoSuchElementException e) {
            return new ResponseEntity<>("Auction doesn't exist!", HttpStatus.FORBIDDEN);
        }
    }

    ResponseEntity<?> removeBidderFromChosenAuction(int auctionId, int bidderId) {
        try {
            Auction auction = auctionRepository.findById(auctionId).orElseThrow();
            List<Integer> list = auction.getBiddersIds();
            if (auction.biddersIds.size() == 0) {
                return new ResponseEntity<>("Currently this auction has no bidders", HttpStatus.FORBIDDEN);
            }
            if (list.contains(bidderId)) {
                Bidder bidder = bidderRepository.findById(bidderId).orElseThrow();
                bidder.setInAuction(false);
                auction.setAuctionersNumber(auction.getAuctionersNumber() - 1);
                list.remove(Integer.valueOf(bidderId));
                auctionRepository.save(auction);
                bidderRepository.save(bidder);

                return new ResponseEntity<>("Succesfully deleted bidder with ID " + bidderId + " from this auction", HttpStatus.OK);
            } else
                return new ResponseEntity<>("This bidder isn't in this auction", HttpStatus.FORBIDDEN);
        } catch (NoSuchElementException e) {
            return new ResponseEntity<>("Auction doesn't exist", HttpStatus.FORBIDDEN);
        }

    }

    ResponseEntity<?> auctionStart(int auctionId) {
        try {
            FileWriter myWriter = new FileWriter("Auction_"+ auctionId +".txt");
            myWriter.write("Auction with ID: "+ auctionId + "\n");
            Random random = new Random();
            Auction auction = auctionRepository.findById(auctionId).orElseThrow();
            if (!auction.isHasBeenFinished() && auction.biddersIds.size() > 1) {


                auction.item.setHasBeenSold(true);
                auction.setHasBeenFinished(true);
                Bidder bidder;
                List<Integer> list = auction.getBiddersIds();

                for (Integer integer : list) {

                    String n = Integer.toString(random.nextInt((50 - 1) + 1) + 1);

                    bidder = bidderRepository.findById(integer).orElseThrow();

                    myWriter.write(bidder.getFirstName() + " " + bidder.getSurname() + " bid: " + n + " million\n");
                    bidder.setValueOfBid(AES.encrypt(n, bidder.getSurname()));
                    bidder.setInAuction(false);
                    bidderRepository.save(bidder);
                }
                Bidder firstBidder;
                Bidder secondBidder;
                for (int m = 0; m < list.size(); m++) {
                    for (int k = 0; k < list.size(); k++) {
                        if (m != k && m <= k) {
                            firstBidder = bidderRepository.findById(list.get(m)).orElseThrow();
                            secondBidder = bidderRepository.findById(list.get(k)).orElseThrow();
                            millionaireProblem(firstBidder, secondBidder);
                        }
                    }
                }
                Bidder winner = new Bidder();
                int winnerNumber = list.size() - 1;
                for (Integer integer : list) {
                    winner = bidderRepository.findById(integer).orElseThrow();
                    if (winner.getWonMillionaireProblemCount() == winnerNumber) {
                        break;
                    }
                }

                auctionRepository.save(auction);
                myWriter.write("This auction has been won by " + winner.getFirstName() + " " + winner.getSurname());
                myWriter.close();
                return new ResponseEntity<>("This auction has been won by " + winner.getFirstName() + " " + winner.getSurname(), HttpStatus.OK);
            } else
                return new ResponseEntity<>("This auction was finished or it has less than 2 bidders, you cannot start it", HttpStatus.FORBIDDEN);
        } catch (NoSuchElementException | IOException e) {
            return new ResponseEntity<>("Auction doesn't exist", HttpStatus.FORBIDDEN);
        }
    }

    private void millionaireProblem(Bidder firstBidder, Bidder secondBidder) {
        Pairs firstBidderPairs = pairsRepository.findById(firstBidder.getBidderId()).orElseThrow();
        BigInteger firstBidderE = new BigInteger(firstBidderPairs.getE());
        BigInteger firstBidderN = new BigInteger(firstBidderPairs.getN());
        BigInteger firstBidderD = new BigInteger(AES.decrypt(firstBidder.getPrivateKey(), firstBidder.getSurname()));
        BigInteger firstBidderValue = new BigInteger(AES.decrypt(firstBidder.getValueOfBid(), firstBidder.getSurname()));
        BigInteger secondBidderValue = new BigInteger(AES.decrypt(secondBidder.getValueOfBid(), secondBidder.getSurname()));
        BigInteger MAX = new BigInteger("50");
        BigInteger X = new BigInteger("3220");

        BigInteger C = X.modPow(firstBidderE, firstBidderN);
        BigInteger m = C.subtract(secondBidderValue).add(BigInteger.ONE);

        ArrayList<BigInteger> Y = new ArrayList<BigInteger>();
        for (BigInteger j = BigInteger.valueOf(0); j.compareTo(MAX) < 0; j = j.add(BigInteger.ONE)) {
            BigInteger m1 = m.add(j);
            BigInteger modpow = m1.modPow(firstBidderD, firstBidderN);
            Y.add(modpow);
        }

        ArrayList<BigInteger> Z = new ArrayList<BigInteger>();
        BigInteger P;

        while (true) {
            BigInteger Pt = new BigInteger(7, 1, new Random());
            if (Pt.isProbablePrime(1)) {
                P = Pt;
                break;
            }
        }

        for (BigInteger j = BigInteger.valueOf(0); j.compareTo(MAX) < 0; j = j.add(BigInteger.ONE)) {
            Z.add(Y.get(j.intValue()).mod(P));
        }

        ArrayList<BigInteger> W = new ArrayList<BigInteger>();
        for (BigInteger i = BigInteger.valueOf(0); i.compareTo(MAX) < 0; i = i.add(BigInteger.ONE)) {
            int result = i.compareTo((firstBidderValue.subtract(BigInteger.ONE)));
            if (result >= 0) {
                W.add((Z.get(i.intValue())).add(BigInteger.ONE));
            } else {
                W.add(Z.get(i.intValue()));
            }
        }

        BigInteger G = X.mod(P);

        int result = G.compareTo(W.get(secondBidderValue.intValue() - 1));
        if (result == 0) {
            firstBidder.setWonMillionaireProblemCount(firstBidder.getWonMillionaireProblemCount() + 1);
            bidderRepository.save(firstBidder);
        } else {
            secondBidder.setWonMillionaireProblemCount(secondBidder.getWonMillionaireProblemCount() + 1);
            bidderRepository.save(secondBidder);
        }

    }


}
